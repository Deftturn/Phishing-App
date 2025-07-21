import HomePage from './Pages/HomePage'
import NavBar from './Component/NavBar'
import { URLProvider } from './URLContext'
import Footer from './Component/Footer'
function App() {


  return (
    <>
      <div className="bg-image min-h-screen">
        <NavBar/>
        <HomePage/>
        <div className="footer">
          <Footer/>
        </div>
      </div>
    </>
  )
}

export default App
