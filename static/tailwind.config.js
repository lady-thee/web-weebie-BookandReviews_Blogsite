/** @type {import('tailwindcss').Config} */
module.exports = {
  mode : 'jit',
  content: [
    "../*/templates/**/*.{html,js}",
  ],
  theme: {
    extend: {
      fontFamily:{
      'del': ['Delicious Handrawn', 'cursive'],
      'sen' : [ 'Sen', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
  ],
}

