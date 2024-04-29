# title: user.py
# Author: Sayan Bandyopadhyay
# Date: 2024-04-09 17:31:18
# Description: This file contains the views that are required for User Page of the FastAPI application.

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse, RedirectResponse

from app.core.config import templates
from app.backend.db.mockdb import users, students, courses, school, calendar
from app.backend.stats import graphs

router = APIRouter()


class HTTPResponseHXRedirect(RedirectResponse):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self["HX-Redirect"] = self["Location"]

    status_code = 200


# These are testing routes for different page views
@router.get("/user/{id}", response_class=HTMLResponse)
async def login(request: Request, id: int):
    for user in users:
        if user.id == id:
            return templates.TemplateResponse(
                "pages/index.html",
                {"request": request, "user": user},
            )
    else:
        return RedirectResponse("/", status_code=303)


@router.get("/graph", response_class=HTMLResponse)
async def graph_view(request: Request):

    # This is a sample graph view for students
    plot = graphs.grade_data()
    return templates.TemplateResponse(
        str(plot),
        {"request": request},
    )
    # TODO: Add more graph views for different models


@router.get("/lists/{type}", response_class=HTMLResponse)
async def list_view(
    request: Request,
    type: str,
    view_page: int = 1,
    view_rows: int = 10,
    sort_by: str = "id",
    invert: bool = False,
):

    types = {
        "students": students,
    }
    dataset = types.get(type, None)  # TODO: Add more models
    cutoff = view_page * view_rows
    if cutoff != 0:
        page_count = (
            (len(dataset) // view_rows) + 1
            if len(dataset) % view_rows != 0
            else len(dataset) // view_rows
        )
        selected = [
            item
            for item in dataset
            if item["id"] <= cutoff and item["id"] > cutoff - view_rows
        ]  # TODO: Change this to actual database query
        sort_selected = sorted(selected, key=lambda x: x[sort_by])
    else:
        sort_selected = sorted(dataset, key=lambda x: x[sort_by])
        page_count = 1
    total_items = len(dataset)
    schools = school
    sort_selected = sort_selected[::-1] if invert else sort_selected
    invert = not invert

    # TODO: Move this to a separate function
    # This is a sample list view for Datasets
    if dataset is None:
        return RedirectResponse("/", status_code=303)

    return templates.TemplateResponse(
        f"partials/lists/{type}.html",
        {
            "request": request,
            "user": users,
            f"{type}": sort_selected,
            f"total_{type}": total_items,
            "schools": schools,
            "page_count": page_count,
            "view_page": view_page,
            "view_rows": view_rows,
            "invert": invert,
        },
    )

    # TODO: Add more list views for different models


@router.get("/courses", response_class=HTMLResponse)
async def courses_view(request: Request):
    dataset = courses
    sort_selected = sorted(dataset, key=lambda x: x["id"])
    total_items = len(dataset)
    schools = school

    return templates.TemplateResponse(
        "pages/courses.html",
        {
            "request": request,
            "user": users[0],
            f"courses": sort_selected,
            f"total_courses": total_items,
            "schools": schools,
        },
    )


@router.get("/student/{id}", response_class=HTMLResponse)
async def student_view(request: Request, id: int):
    tabs = [
        {
            "header": "Overview",
        },
        {
            "header": "Courses",
        },
        {
            "header": "Assessments",
        },
        {
            "header": "Calendar",
        },
        {
            "header": "Moodle",
        },
        {
            "header": "Shared Notes",
        },
        {
            "header": "Self Reports",
        },
    ]
    for student in students:
        if student["id"] == id:
            return templates.TemplateResponse(
                "pages/student.html",
                {
                    "request": request,
                    "user": users[1],  # TODO: Change this to actual user
                    "student": student,
                    "tabs": tabs,
                },
            )
    else:
        return RedirectResponse("/", status_code=303)


@router.get("/calendar", response_class=HTMLResponse)
async def calendar_view(request: Request):
    events = calendar
    sorted_events = sorted(events, key=lambda x: x["due_date"])
    return templates.TemplateResponse(
        "pages/calendar.html",
        {
            "request": request,
            "user": users[0],
            "events": sorted_events,
        },  # TODO: Change this to actual user
    )
