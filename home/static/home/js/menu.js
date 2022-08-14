let menuBtn = document.getElementsByClassName('NavSmMenu')[0]
let menuSm = document.getElementsByClassName('navSm')[0]
let menuInner = document.getElementsByClassName('navSm__inner')[0]
let menuBtnAct = false


menuBtn.addEventListener('click', function(){
    if(menuBtnAct == false){
        menuBtnAct = true
        menuInner.classList.add('menuBtnActive')
        menuSm.classList.add('navSmActive')
        
    }
    else if(menuBtnAct == true){
        menuBtnAct = false
        menuInner.classList.remove('menuBtnActive')
        menuSm.classList.remove('navSmActive')
    }
})