//Creacion de ubicacion localizacion local google map api
let map;
async function initMap() {
  let coord  = {lat:-33.012516 ,lng:-71.549197 };
  const { Map } = await google.maps.importLibrary("maps");
  map = new Map(document.getElementById("map"), {
    center: coord,
    zoom: 16,
  });
  var marker = new google.maps.Marker({
    position: coord,
    map: map
});
}
initMap();


//Obtencion datos API openweathermap
let key = 'b2158dabed90c6c3a9797b6e96405750';
let ciudad = document.getElementById('city');
let boton = document.getElementById('btn');
let resultado = document.getElementById('resultado');
let get_weather = () => {
  let city_name = ciudad.value;
    let url = `https://api.openweathermap.org/data/2.5/weather?q=${city_name}&appid=${key}&units=metric`
    fetch(url).then((resp) => resp.json()).then(data => {
      console.log("la temperatura es " +(data.main.temp)+'°');
      console.log(data.weather[0].description);
      console.log(data);
      resultado.innerHTML = `<h2>${data.name} | ${data.main.temp+'°'}</h2>`
    });
}
boton.addEventListener('click',get_weather);