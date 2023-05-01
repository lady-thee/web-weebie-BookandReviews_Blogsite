/**
 * Close message tags
 */


const messagebody = document.querySelectorAll('#messagebody')
const closemessage = document.querySelectorAll('#close_message')

let onclick = (e) => {
    messagebody.forEach((item) =>{
        item.style.display = 'none'
    })
}

// closemessage.addEventListener('click', () =>{
//     messagebody.style.display = 'none';
// })

closemessage.forEach((item) =>{
    item.addEventListener('click', onclick);
})
