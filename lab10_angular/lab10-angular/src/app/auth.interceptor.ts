import { HttpRequest, HttpInterceptor, HttpHandler, HttpEvent, HttpErrorResponse, HttpResponse } from '@angular/common/http'
import { Injectable } from '@angular/core'
import { Observable } from 'rxjs'

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  constructor() {}

  intercept(
    req: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
      const token = localStorage.getItem('token');
      if(token){
        const authReq = req.clone({
            headers: req.headers.append('Authorization', `JWT ${token}`)
          });
          return next.handle(authReq);
      }
    console.log('no token in local storage');

    return next.handle(req)
        
      
    
  }
}