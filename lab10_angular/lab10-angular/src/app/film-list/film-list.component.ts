import { Component, OnInit } from '@angular/core';
import { Company } from '../company';
import { CompanyService } from '../films.service';
@Component({
  selector: 'app-film-list',
  templateUrl: './film-list.component.html',
  styleUrls: ['./film-list.component.css']
})
export class FilmListComponent implements OnInit {
  companies: Company[];
  constructor(private companyService: CompanyService) { }

  ngOnInit(): void {
    console.log(this.companies);
    
    this.getCompanies();
    
  }
  getCompanies(): void{
    this.companyService.getCompanies().subscribe(companies => this.companies = companies);
  }
}
