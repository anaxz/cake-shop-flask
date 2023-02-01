// import prices from '../customOrderPrices';

const cakeSize = document.getElementById('cake-size');
const cakeFlavour = document.getElementById('cake-flavour');

// fruit toppings
const topStrawberry = document.getElementById('toppings-strawberry')
const topMango = document.getElementById('toppings-mango')
const topKiwi = document.getElementById('toppings-kiwi')

// fruit fillings
const fillingStrawberry = document.getElementById('fillings-strawberry')
const fillingMango = document.getElementById('fillings-mango')
const fillingKiwi = document.getElementById('fillings-kiwi')

const price = document.getElementById('price')
const submitBtn = document.getElementById("submit-btn");

function displayBtns(val){
    submitBtn.disabled = val;
}

function handleGetQuote(e){
    console.log('get quote!')
    displayBtns()
    // console.log(price.)

    
}