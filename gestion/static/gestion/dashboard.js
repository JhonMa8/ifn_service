document.addEventListener("DOMContentLoaded", () => {
  // 1. Extraer token y rol desde URL si existen
  const params = new URLSearchParams(window.location.search);
  const tokenFromURL = params.get("token");
  const roleFromURL = params.get("role");

  // 2. Guardar en localStorage si vienen de la URL
  if (tokenFromURL && roleFromURL) {
    localStorage.setItem("token", tokenFromURL);
    localStorage.setItem("role", roleFromURL);

    // Quitar los parámetros de la URL
    history.replaceState(null, "", "/dashboard/");
  }

  // 3. Leer rol desde localStorage
  const role = localStorage.getItem("role");
  const roleSpan = document.getElementById("userRole");

  if (!role) {
    roleSpan.textContent = "Desconocido";
    alert("No se detectó un rol válido. Redirigiendo al login.");
    window.location.href = "http://127.0.0.1:8000/";
    return;
  }

  // 4. Mostrar el rol y su menú correspondiente
  roleSpan.textContent = role;

  if (role === "admin") {
    document.getElementById("menuAdmin").style.display = "block";
  } else if (role === "jefe_brigada") {
    document.getElementById("menuJefe").style.display = "block";
  } else if (role === "tecnico") {
    document.getElementById("menuTecnico").style.display = "block";
  } else if (role === "botanico") {
    document.getElementById("menuBotanico").style.display = "block";
  } else {
    roleSpan.textContent = "Rol no reconocido";
  }
});
