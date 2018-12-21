# sunspot.academy

## Installation

* Prepare Python Environment
    ```
    pipenv install --dev
    pipenv shell
    ```
* Prepare JavaScript Environment
   ```
   yarn install
   ```
* Start Backend Server
   ```
   python run.py
   ```
* Start Webpack Server
   ```
   yarn serve
   ```


## Deploy

This website is currently hosted on Heroku.

* Create new app on heroku and connect the repo

## Development

This website is built on flask and vue+webpack. The backend located at `app/*` is the API that provides the data interface. The frontend located at `src/*` and `public/*` is in charge of the interactions with API and the user interfaces.

`yarn install` will install the packages specified in the file `package.json`. `yarn build` will generate the static pages and place them in the folder `dist`. Then flask will render these frontend assets live when we excute `python run.py`.

## References

1. [gtalarico/flask-vuejs-template](https://github.com/gtalarico/flask-vuejs-template)
2. [Flask + MongoDB Tutorial](https://www.youtube.com/watch?v=upGiAG7-Sa4)
