import React, { useState, useEffect } from "react";


const ProductCategories = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    
    fetch("http://127.0.0.1:5000/")
      .then((response) => response.json())
      .then((data) => {
        setProducts(data.products);
      })
      .catch((error) => console.log("Error fetching products:", error));
  }, []);

  const handleBuyNow = (productName) => {
    alert(`You have bought the product: ${productName}`);
  };

  return (
    <div className="product-categories">
      <h2>Our Products</h2>
      <div className="product-grid">
        {products.length > 0 ? (
          products.map((product) => (
            <div key={product.id} className="product-card">
              
              <img
                src={`data:image/png;base64,${product.image}`}
                alt={product.name}
                className="product-image"
              />
              <h3>{product.name}</h3>
              <p><strong>Category:</strong> {product.category}</p>
              <p><strong>Price:</strong> ₹{product.price}</p>
              <p><strong>Description:</strong> {product.description}</p>

              
              <button onClick={() => handleBuyNow(product.name)}>Buy Now</button>
            </div>
          ))
        ) : (
          <p>No products available</p>
        )}
      </div>
    </div>
  );
};

export default ProductCategories;
