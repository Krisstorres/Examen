Element.prototype.remove = function() {
    this.parentElement.removeChild(this);
  }
  NodeList.prototype.remove = HTMLCollection.prototype.remove = function() {
    for(var i = this.length - 1; i >= 0; i--) {
        if(this[i] && this[i].parentElement) {
            this[i].parentElement.removeChild(this[i]);
        }
    }
  }



$(document).ready(function() {
    $('#div-btn1').on('click', function() {
        $('.navbar-nav li').removeClass('active');
        $("#central").load('php/QuienesSomos.php');
        return false;
    });

    $('#div-btn2').on('click', function() {
        $('.navbar-nav li').removeClass('active');
        $("#central").load('php/Tienda.php');
        return false;
    });

    $('#div-btn3').on('click', function() {
        $('.navbar-nav li').removeClass('active');
        $("#central").load('php/Donaciones.php');
        return false;
    });

    $('#div-btn4').on('click', function() {
        $('.navbar-nav li').removeClass('active');
        $("#central").load('php/Contacto.php');
        return false;
    }); 


$('#div-btn5').on('click', function() {
    $('.a').removeClass('activee');
    $("#central").load('php/QuienesSomos.php');
    return false;
}); 

$('#div-btn6').on('click', function() {
  $('.a').removeClass('activee');
  $("#central").load('php/Tienda.php');
  return false;
}); 

$('#div-btn7').on('click', function() {
  $('.a').removeClass('activee');
  $("#central").load('php/Donaciones.php');
  return false;
}); 

$('#div-btn8').on('click', function() {
  $('.a').removeClass('activee');
  $("#central").load('php/Contacto.php');
  return false;
}); 



$('#div-btn9').on('click', function() {
  $('.a').removeClass('activeee');
  $("#central").load('php/Tienda.php');
  return false;
}); 

$('#div-btn10').on('click', function() {
  $('.a').removeClass('activeee');
  $("#central").load('php/Tienda.php');
  return false;
}); 

$('#div-btn11').on('click', function() {
  $('.a').removeClass('activeee');
  $("#central").load('php/Tienda.php');
  return false;
}); 

$('#div-btn12').on('click', function() {
  $('.a').removeClass('activeee');
  $("#central").load('php/Tienda.php');
  return false;
}); 

$('#div-btn13').on('click', function() {
  $('.a').removeClass('activeee');
  $("#central").load('php/Tienda.php');
  return false;
}); 

$('#div-btn14').on('click', function() {
  $('.a').removeClass('activeee');
  $("#central").load('php/Donaciones.php');
  return false;
}); 

$('#div-btn15').on('click', function() {
  $('.a').removeClass('activee');
  $("#central").load('php/Tienda.php');
  return false;
}); 

$('#div-btn16').on('click', function() {
  $('.a').removeClass('activee');
  $("#central").load('php/Contacto.php');
  return false;
}); 





$('#div-btn21').on('click', function() {
  alert("ddd")
  $('.navbar-nav li').removeClass('eee');
  $("#central").load('php/QuienesSomos.php');
  return false;
});

$('#div-btn22').on('click', function() {
  $('.navbar-nav li').removeClass('eee');
  $("#central").load('php/Tienda.php');
  return false;
});

$('#div-btn23').on('click', function() {
  $('.navbar-nav li').removeClass('eee');
  $("#central").load('php/Donaciones.php');
  return false;
});

$('#div-btn24').on('click', function() {
  $('.navbar-nav li').removeClass('eee');
  $("#central").load('php/Contacto.php');
  return false;
}); 



$('#div-btn31').on('click', function() {
  $('.navbar-nav li').removeClass('eee');
  $("#central").load('php/Tienda.php');
  return false;
});

$('#div-btn32').on('click', function() {
  $('.navbar-nav li').removeClass('eee');
  $("#central").load('php/Tienda.php');
  return false;
});

$('#div-btn33').on('click', function() {
  $('.navbar-nav li').removeClass('eee');
  $("#central").load('php/Tienda.php');
  return false;
});

$('#div-btn34').on('click', function() {
  $('.navbar-nav li').removeClass('eee');
  $("#central").load('php/Tienda.php');
  return false;
}); 




});













