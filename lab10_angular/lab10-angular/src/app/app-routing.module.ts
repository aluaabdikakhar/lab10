import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { FilmListComponent } from './film-list/film-list.component';
import { FilmDetailComponent } from './film-detail/film-detail.component';


const routes: Routes = [
  {path: 'films', component: FilmListComponent},
  {path: '', redirectTo: '/films', pathMatch: 'full'},
  {path: 'films/:id', component: FilmDetailComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
