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
  async authUser(){
    try{
      const result = await this.usuarioService.authenticate(this.username, this.password).toPromise();
      this.router.navigate(['/inicio']); 
      console.log(result);
    }catch(error){
      this.timerDialog("USUARIO INCORRECTO");
      console.log(error);
    }
  }

  timerDialog(mensaje : string){
    this.mostrarDialog = true;
    this.mensaje = mensaje;
    setTimeout(() => {
      this.mostrarDialog = false;
    }, 4000);
  }
}

