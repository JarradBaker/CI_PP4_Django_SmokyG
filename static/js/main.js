const hamburger = document.getElementsByClassName('hamburger')[0];
const navLinksMobile = document.getElementsByClassName('nav-links-mobile')[0];
const editComment = document.getElementsByClassName('edit-comment')
const deleteComment = document.getElementsByClassName('delete-comment')
const deleteAlert = document.getElementsByClassName('btn-close')

/**
 * Event listener to toggle the hamburger menu and nav links
 */
hamburger.addEventListener('click', () => {
    if(navLinksMobile.getAttribute('class', 'hide')){
        navLinksMobile.removeAttribute('class', 'hide');
    } else {
        navLinksMobile.classList.add('hide');
    } 
} );

deleteAlert.addEventListener('click', () => {
    deleteAlert.classList.add('hide');
});