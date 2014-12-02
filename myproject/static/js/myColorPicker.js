// Color pickers in different flavors.
// -----------------------------------

var cpDefault = ColorPicker(document.getElementById('color-picker-popup'), updateInputs);

// Inputs.
// -------

function updateInputs(hex) {
    $("#profile-header-popup").css({'background':'url(../images/bg-tissue.png),-webkit-gradient(radial, 50% 50%, 0, 50% 50%, 287, color-stop(0%, '+ hex +'), color-stop(100%, #000))'});
}

function updateColorPickers(hex) {
    
    cpDefault.setHex(hex);
}


var initialHex = '#f4329c';
updateColorPickers(initialHex);

