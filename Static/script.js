function copiarEmail() {
    var email = document.getElementById("email");
    navigator.clipboard.writeText(email.value).then(function() {
        alert('Email copiado: ' + email.value);
    }, function(err) {
        alert('Error al copiar el email: ' + err);
    });
}

function toggleMenu() {
    var mobileMenu = document.getElementById("mobile-menu");
    mobileMenu.style.display = (mobileMenu.style.display === "block") ? "none" : "block";
}


