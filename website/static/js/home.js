function cake_link(e){
    console.log('cake link clicked')
    // fetch('/custom-order')
}

async function customOrder_link(e){
    console.log('custom order clicked')
    try {
        fetch('http://127.0.0.1:5000/custom-order')
    } catch(err){
        return err
    }
}