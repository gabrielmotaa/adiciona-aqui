const addressBtn = document.getElementById("address-btn");
const addressField = document.getElementById("id_address");

if (addressBtn && addressField) {
  addressBtn.addEventListener("click", getLocationAddress);
}

async function makeOpenStreetRequest(longitude, latitute) {
  const response = await fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitute}&lon=${longitude}`);
  if (!response.ok)
    throw Error("Erro ao fazer a requisição. Status: " + response.status);
  const json = await response.json();
  return json;
}

function getLocationAddress() {
  if (!navigator.geolocation) {
    console.warning("O serviço de geolocalização não está disponível");
    return;
  }

  const onSuccess = (position) => {
    makeOpenStreetRequest(position.coords.longitude, position.coords.latitude)
      .then((json) => addressField.value = json.address.road)
      .catch(console.error);
  };

  const onError = () => console.error("Erro ao coletar informação de localização");

  navigator.geolocation.getCurrentPosition(onSuccess, onError);
}
