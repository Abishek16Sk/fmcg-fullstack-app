import React from 'react';
import './App.css'
import Header from './components/Header'; 
import HeroSection from './components/HeroSection'; 
import ProductCategories from './components/ProductCategories';
import Footer from './components/Footer';

function App() {
  return (
    <div className="App">
      <Header /> 
      <HeroSection /> 
      <ProductCategories />
      <Footer />
    </div>
  );
}

export default App;
