// dashboard.js

document.addEventListener("DOMContentLoaded", () => {
    // 1) Extraer token y role de la URL
    const params = new URLSearchParams(window.location.search);
    const token = params.get("token");
    const role  = params.get("role");
  
    // 2) Si vienen en la URL, guardarlos en localStorage
    if (token && role) {
      localStorage.setItem("token", token);
      localStorage.setItem("role", role);
      // Limpiar la URL para que no se vean en la barra
      history.replaceState(null, "", "dashboard/");
    }
  
    // 3) Mostrar el rol en pantalla
    const roleSpan = document.getElementById("userRole");
    const savedRole = localStorage.getItem("role");
  
    if (!savedRole) {
      roleSpan.textContent = "Desconocido";
      alert("No se detectó un rol válido. Redirigiendo al login.");
      window.location.href = "http://127.0.0.1:8000/";  // o index.html de login-service
      return;
    }
  
    roleSpan.textContent = savedRole;
  
    // 4) Mostrar menú según rol
    switch (savedRole) {
      case "admin":
        document.getElementById("menuAdmin").style.display = "block";
        break;
      case "jefe_brigada":
        document.getElementById("menuJefe").style.display = "block";
        break;
      case "tecnico":
        document.getElementById("menuTecnico").style.display = "block";
        break;
      case "botanico":
        document.getElementById("menuBotanico").style.display = "block";
        break;
      default:
        roleSpan.textContent = "Rol no reconocido. Contacta al admin.";
    }
  });
  