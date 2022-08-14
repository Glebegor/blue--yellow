$('#id_number').on('keypress', function (event) {
    console.log(event.charCode)
    console.log(event.which)
    var regex = new RegExp("^[0-9]+$");
    var key = String.fromCharCode(!event.charCode ? event.which : event.charCode);
    console.log(regex.test(key))
    if (!regex.test(key)) {
       event.preventDefault();
       return false;
    }
});