import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {HttpClientModule, HTTP_INTERCEPTORS} from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FilmListComponent } from './film-list/film-list.component';
import { FilmDetailComponent } from './film-detail/film-detail.component';
import { TopBarComponent } from './top-bar/top-bar.component';
import {FormsModule} from '@angular/forms';
import { AuthInterceptor } from './auth.interceptor';
@NgModule({
  declarations: [
    AppComponent,
    FilmListComponent,
    FilmDetailComponent,
    TopBarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
