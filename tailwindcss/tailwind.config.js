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
    themes: [
      {
        myPathLight: {
          "color-scheme": "light",
          "primary": "#04365e",
          "primary-content": "#074e88",
          "secondary": "#0d6bb9",
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
    base: true, // applies background color and foreground color for root element by default
    styled: true, // include daisyUI colors and design decisions for all components
    utils: true, // adds responsive and modifier utility classes
    prefix: "", // prefix for daisyUI classnames (components, modifiers and responsive class names. Not colors)
    logs: true, // Shows info about daisyUI version and used config in the console when building your CSS
    themeRoot: "*", // The element that receives theme color CSS variables
  },
}
