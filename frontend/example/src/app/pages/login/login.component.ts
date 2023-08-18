import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { UsuarioService } from 'src/app/services/usuario.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username : string = "";
  password : string =  "";
  mensaje = ""
  mostrarDialog = false;

  constructor(private usuarioService:UsuarioService, private router: Router,private activatedRouter : ActivatedRoute){}
async authUser() {
  this.usuarioService.authenticate(this.username, this.password).subscribe(
    (data: any) => {
      this.timerDialog('Correcto!!');
    },
    (error: any) => {

      this.timerDialog('Usuario o contraseña incorrectos');
    }
  );
}



  timerDialog(mensaje : string){
    this.mostrarDialog = true;
    this.mensaje = mensaje;
    setTimeout(() => {
      this.mostrarDialog = false;
    }, 4000);
  }
  
}

