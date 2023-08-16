import { Component } from '@angular/core';
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

  constructor(private usuarioService:UsuarioService){}
  async authUser(){
    try{
      const result = await this.usuarioService.authenticate(this.username, this.password).toPromise();
      this.mensaje = "USUARIO CORRECTO"
      console.log(result);
    }catch(error){
      this.mensaje = "USUARIO INCORRECTO"
      console.log(error);
    }
  }
}
