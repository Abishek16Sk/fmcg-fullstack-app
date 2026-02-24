import React, { useEffect, useState } from "react";

const HeroSection = () => {
  const [products, setProducts] = useState([]);
  const [currentSlide, setCurrentSlide] = useState(0);

  useEffect(() => {
    // Fetch product data from the backend
    fetch("http://127.0.0.1:5000/")
      .then((response) => response.json())
      .then((data) => {
        setProducts(data.products);
      })
      .catch((error) => console.log("Error fetching products:", error));
  }, []);

  useEffect(() => {
    // Automatically switch slides every 3 seconds
    const slideInterval = setInterval(() => {
      setCurrentSlide((prevSlide) =>
        prevSlide === products.length - 1 ? 0 : prevSlide + 1
      );
    }, 3000);

    return () => clearInterval(slideInterval); // Cleanup interval on component unmount
  }, [products]);

  return (
    <div className="hero-section">
      {products.length > 0 ? (
        <div className="slideshow-container">
          {products.map((product, index) => (
            <div
              key={index}
              className={`mySlides fade ${
                index === currentSlide ? "active" : "inactive"
              }`}
            >
              <img
                src={`data:image/png;base64,${product.image}`}
                alt={product.name}
                className="slide-image"
              />
              <div className="product-info">
                <h2>{product.name}</h2>
                <p>
                  <strong>₹{product.price}</strong>
                </p>
              </div>
            </div>
          ))}
        </div>
      ) : (
        <p>No products available</p>
      )}
    </div>
  );
};

export default HeroSection;
