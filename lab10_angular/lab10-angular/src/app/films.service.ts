import { Injectable } from '@angular/core';
import { Company } from './company';
import { Observable, of} from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Vacancy } from './vacancy';
@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  BASE_URL = 'http://localhost:8000';
  constructor(private http: HttpClient) { }
  getCompanies(): Observable<Company[]>{
    return this.http.get<Company[]>(`${this.BASE_URL}/api/companies/`);    
    // return of(films);
  }
  getFilm(id: number): Observable<Company> {
    return this.http.get<Company>(`${this.BASE_URL}/api/companies/${id}/`)
 
    // return of(films.find(film => film.id === id));
  }
  getVacancies(id: number): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`${this.BASE_URL}/api/companies/${id}/vacancies/`)
  }
  login(username, password){
    return this.http.post(`${this.BASE_URL}/api/login/`, {
      username: username,
      password: password
    })
  }
}
