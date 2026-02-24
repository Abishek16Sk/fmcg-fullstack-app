import React, { useState, useEffect } from "react";

const ProductCategories = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/products")
      .then((res) => res.json())
      .then((data) => {
        setProducts(Array.isArray(data) ? data : []);
      })
      .catch((error) => {
        console.log("Error fetching products:", error);
        setProducts([]);
      });
  }, []);

  const handleBuyNow = (productName) => {
    alert(`You have bought the product: ${productName}`);
  };

  return (
    <div className="product-categories">
      <h2>Our Products</h2>

      <div className="product-grid">
        {products.length === 0 ? (
          <p>No products available</p>
        ) : (
          products.map((product, index) => (
            <div key={index} className="product-card">
              <img
                src={product.image_url || "https://via.placeholder.com/200"}
                alt={product.name}
                className="product-image"
              />

              <h3>{product.name}</h3>
              <p><strong>Category:</strong> {product.category}</p>
              <p><strong>Price:</strong> ₹{product.price}</p>
              <p><strong>Description:</strong> {product.description}</p>

              <button onClick={() => handleBuyNow(product.name)}>
                Buy Now
              </button>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default ProductCategories;