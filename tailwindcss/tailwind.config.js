/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../app/templates/**/*.{html,js}",
    "../app/src/**/*.{html,js}",
    "../app/templates/partials/navigation/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ['forest', 'light',
      {
        myPathDark: {
          "color-scheme": "dark",
          "primary": "#023660",
          "primary-content": "#03223b",
          "secondary": "#068af0",
          "secondary-content": "#fff",
          "accent": "#eab218",
          "neutral": "#2b323b",
          "neutral-content": "#a0a6b4",
          "base-100": "#2b323b",
          "base-200": "#1a1f24",
          "base-300": "#161a20",
          "info": "#00aefc",
          "success": "#00a36c",
          "warning": "#feb700",
          "error": "#ff565e",
        },
        myPathLight: {
          "color-scheme": "light",
          "primary": "#04365e",
          "primary-content": "#074e88",
          "secondary": "#377cfb",
          "secondary-content": "#fff",
          "accent": "#f4b913",
          "accent-content": "#000",
          "neutral": "#333c4d",
          "neutral-content": "#f9fafb",
          "base-100": "oklch(100% 0 0)",
          "base-content": "#333c4d",
          "info": "#00aefc",
          "success": "#00a36c",
          "warning": "#feb700",
          "error": "#ff565e",
        }
      }], // false: only light + dark | true: all themes | array: specific themes like this ["light", "dark", "cupcake"]
    darkTheme: 'myPathDark', // name of one of the included themes for dark mode
    base: true, // applies background color and foreground color for root element by default
    styled: true, // include daisyUI colors and design decisions for all components
    utils: true, // adds responsive and modifier utility classes
    prefix: "", // prefix for daisyUI classnames (components, modifiers and responsive class names. Not colors)
    logs: true, // Shows info about daisyUI version and used config in the console when building your CSS
    themeRoot: "*", // The element that receives theme color CSS variables
  },
}
