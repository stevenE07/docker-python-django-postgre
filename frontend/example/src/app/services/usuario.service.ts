import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  constructor(private http : HttpClient) { }

  authenticate(username:string, password:string){
    return this.http.post(`localhost:8000/polls/authenticate`, { username, password });
  }
}
