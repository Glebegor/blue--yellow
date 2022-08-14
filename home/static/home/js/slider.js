// Slider__point
const slideContainer = document.querySelector('.Slider__inner');
const slide = document.querySelector('.Slider');
const nextBtn = document.getElementsByClassName('NextSlider')[0];
const prevBtn = document.getElementsByClassName('PrevSlider')[0];
const interval = 3000;

let point__item = document.getElementsByClassName('point__item')


let slides = document.querySelectorAll('.Slider__item');
let index = 1;
let indexSlider = 0;
let slideId;

const firstClone = slides[0].cloneNode(true);
const lastClone = slides[slides.length - 1].cloneNode(true);

firstClone.id = 'first-clone';
lastClone.id = 'last-clone';

slide.append(firstClone);
slide.prepend(lastClone);

const slideWidth = slides[index].clientWidth;

slide.style.transform = `translateX(${-slideWidth * index}px)`;
const startSlide = () => {
  slideId = setInterval(() => {
    moveToNextSlide();
  }, interval);
};

const getSlides = () => document.querySelectorAll('.Slider__item');

slide.addEventListener('transitionend', () => {
  slides = getSlides();
  if (slides[index].id === firstClone.id) {
    point__item[0].classList.add('PointActive')
    point__item[indexSlider-1].classList.remove('PointActive')
    indexSlider = 0;
    slide.style.transition = 'none';
    index = 1;
    slide.style.transform = `translateX(${-slideWidth * index}px)`;
  }

  if (slides[index].id === lastClone.id) {
    point__item[point__item.length - 1].classList.add('PointActive')
    point__item[0].classList.remove('PointActive')
    indexSlider = point__item.length - 1;
    slide.style.transition = 'none';
    index = slides.length - 2;
    slide.style.transform = `translateX(${-slideWidth * index}px)`;
  }
});

const moveToNextSlide = () => {
  slides = getSlides();
  if (index >= slides.length - 1) return;
  index++;
  indexSlider++;
  if(slides[index].id === firstClone.id){
    
  }else{
    point__item[indexSlider].classList.add('PointActive')
    point__item[indexSlider-1].classList.remove('PointActive')
  }
  slide.style.transition = '.7s ease-out';
  slide.style.transform = `translateX(${-slideWidth * index}px)`;
};

const moveToPreviousSlide = () => {
  if (index <= 0) return;
  index--;
  indexSlider--;
  if(slides[index].id === lastClone.id){

  }else{
    point__item[indexSlider].classList.add('PointActive')
    point__item[indexSlider+1].classList.remove('PointActive')
  }
  slide.style.transition = '.7s ease-out';
  slide.style.transform = `translateX(${-slideWidth * index}px)`;
};

slideContainer.addEventListener('mouseenter', () => {
  clearInterval(slideId);
});

slideContainer.addEventListener('mouseleave', startSlide);
nextBtn.addEventListener('click', moveToNextSlide);
prevBtn.addEventListener('click', moveToPreviousSlide);

startSlide();
