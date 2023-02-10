import customPrices from '../customOrderPrices.json' assert {type: 'json'};

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

const quoteBtn = document.getElementById('quote-btn');

quoteBtn.addEventListener('click', (e) => {
    console.log('get quote!')
    displayBtns()
    
    // price.textContent = '£'+totalPrice()
    price.value = totalPrice()
} )

function updatePrice(){
    price.value = '£'+totalPrice()
}

// display submit btn when get quote is clicked
function displayBtns(val){
    submitBtn.disabled = val;
}

// hide checkbox if reach limit
function hideCheckbox(){

}

function getPrice(type, input){
    const val = type.find((index) => {
        for (let [key, value] of Object.entries(index)) {
            // console.log(`${key}: ${value}`);
            if(input === key) return value;
        }
    })
    return parseFloat(Object.values(val))
}

function checkboxGetPrice(checkedItems){
    let val = 0;
    for(let i = 0; i < checkedItems.length; i++){
        val += getPrice(customPrices.toppings, checkedItems[i])
    }
    return val;
}

function getCheckedItems(type){
    let checkedItems = []; 
    for(let i=0; i < type.length; ++i){
        if(type[i].checked) checkedItems.push(type[i].value)
    }
    return checkedItems
}

function totalPrice(){
    const sizePrice = getPrice(customPrices.size, cakeSize.value)
    console.log(sizePrice)

    const flavourPrice = getPrice(customPrices.flavour, cakeFlavour.value)
    console.log(flavourPrice)

    let toppings = document.getElementsByClassName('toppings');
    const toppingsPrice = checkboxGetPrice(getCheckedItems(toppings))
    console.log(toppingsPrice)

    let fillings = document.getElementsByClassName('fillings');
    const fillingsPrice = checkboxGetPrice(getCheckedItems(fillings))
    console.log(fillingsPrice)

    const sum = sizePrice + flavourPrice + toppingsPrice + fillingsPrice
    return Math.round(sum * 100)/100;
    // return Number.toFixed(sum)
}