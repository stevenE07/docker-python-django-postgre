import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  constructor(private http : HttpClient) { }

  authenticate(email:string, password:string){
    return this.http.post(`http://127.0.0.1:8000/login/`, {'username':email, 'password':password});
  }

  prueba(){
    return this.http.post('https://retoolapi.dev/q2J3Ni/data', {})
  }
}
