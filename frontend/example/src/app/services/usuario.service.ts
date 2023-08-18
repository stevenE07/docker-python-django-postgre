import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  constructor(private http : HttpClient) { }

  authenticate(username:string, password:string){
    // with cors headers
    return this.http.post(`http://localhost:8000/polls/authenticate`, {username, password});
  }

  prueba(){
    return this.http.post('https://retoolapi.dev/q2J3Ni/data', {})
  }
}
