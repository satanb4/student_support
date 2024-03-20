/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../app/templates/**/*.{html,js}","../app/src/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: [
      {
        maintheme: {
          "primary": "#8600ff",    
          "secondary": "#ff0000",
          "accent": "#f18d00",
          "neutral": "#0c0403",
          "base-100": "#2c2f2a",
          "info": "#00d6ff",
          "success": "#009314",
          "warning": "#9c6800",
          "error": "#ff7879",
        },
      },
    ],
  },
}

