import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CompanyService } from '../films.service';
import { Company } from '../company';
import { Vacancy } from '../vacancy';

@Component({
  selector: 'app-film-detail',
  templateUrl: './film-detail.component.html',
  styleUrls: ['./film-detail.component.css']
})
export class FilmDetailComponent implements OnInit {
  company: Company;
  vacancies: Vacancy[];
  constructor(private route: ActivatedRoute,
    private companyService: CompanyService) { }

  ngOnInit(): void {
    this.getFilm();
  }
  getFilm(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    console.log(id);
    
    this.companyService.getFilm(id).subscribe(company => this.company = company);
    this.companyService.getVacancies(id).subscribe(vacancies => this.vacancies = vacancies);
  }
  
}
