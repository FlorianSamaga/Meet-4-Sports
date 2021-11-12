if (process.env.NODE_ENV !== 'production') {
    require('dotenv').config()
}


const express = require('express')
const app = express()
const bcrypt = require('bcrypt')
const passport = require('passport')
const flash = require('express-flash')
const session = require('express-session')
const methodOverride = require('method-override')



const initializePassport = require('./passport-config')
initializePassport(
    passport,
    email => users.find(user => user.email === email),
    id => users.find(user => user.id === id)
)

const users = []

app.set('view-engine', 'ejs')
app.use(express.urlencoded({ extended: false }))
app.use(flash())
app.use(session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: false
}))
app.use(passport.initialize())
app.use(passport.session())
app.use(methodOverride('_method'))


//Benutzer wird auf die Startseite geleitet, sofern er angemeldet ist.
app.get('/', checkAuthenticated, (req, res) => {
    res.render('index.ejs', { name: req.user.name })
})

//Benutzer wird auf Loginseite geleitet, sofern er nicht schon angemeldet ist.
app.get('/login', checkNotAuthenticated, (req, res) => {
    res.render('login.ejs')
})
//Benutzer wird angemeldet, sofern er nicht schon angemeldet ist.
app.post('/login', checkNotAuthenticated, passport.authenticate('local', {
    successRedirect: '/',
    failureRedirect: '/login',
    failureFlash: true
}))
//Benutzer wird auf Registrierseite geleitet, sofern er nicht schon angemeldet ist.
app.get('/register', checkNotAuthenticated, (req, res) => {
    res.render('register.ejs')
})
//Neuer Benutzer wird registriert, sofern er gerade nicht schon angemeldet ist.
app.post('/register', checkNotAuthenticated, async (req, res) => {
    try {
        const hashedPassword = await bcrypt.hash(req.body.password, 10)
        users.push({
            id: Date.now().toString(),
            name: req.body.name,
            email: req.body.email,
            password: hashedPassword
        })
        res.redirect('/login')
    } catch {
        res.redirect('/register')
    }
})

//Benutzer wird abgemeldet und auf Loginseite weitergeleitet, sofern er angemeldet ist.
//(Benutzer kann die Seite eh nur erreichen wenn er angemeldet ist.)
app.delete('/logout', checkAuthenticated, (req, res) => {
    req.logOut()
    res.redirect('/login')
})

//Benutzer wird auf die Startseite geleitet, sofern er angemeldet ist.
app.get('/', checkAuthenticated, (req, res) => {
    res.render('index.ejs', { name: req.user.name })
})

//Überprüft, ob der Benutzer angemeldet ist. Falls ja wird fortgefahren, falls nein wird
//der Benutzer auf die Login Seite geleitet.
function checkAuthenticated(req, res, next) {
    if (req.isAuthenticated()) {
        return next()
    }

    res.redirect('/login')
}





//Überprüft, ob der Benutzer schon angemeldet ist. Falls ja wird der Benutzer auf die Startseite
//geleitet, falls nein wird fortgefahren
function checkNotAuthenticated(req, res, next) {
    if (req.isAuthenticated()) {
        return res.redirect('/')
    }
    next()
}
//Portzuweisung
app.listen(3000)