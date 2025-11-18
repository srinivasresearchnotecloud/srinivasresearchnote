import streamlit as st

st.set_page_config(page_title="E-Commerce Demo", layout="wide")

# ---------------------------
# PRODUCT DATA
# ---------------------------
products = [
    {"id": 1, "name": "Laptop", "price": 55000, "img": "https://via.placeholder.com/150"},
    {"id": 2, "name": "Smartphone", "price": 30000, "img": "https://via.placeholder.com/150"},
    {"id": 3, "name": "Headphones", "price": 2500, "img": "https://via.placeholder.com/150"},
    {"id": 4, "name": "Smartwatch", "price": 7000, "img": "https://via.placeholder.com/150"},
    {"id": 5, "name": "Keyboard", "price": 1200, "img": "https://via.placeholder.com/150"},
]

# ---------------------------
# SESSION CART
# ---------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# ---------------------------
# FUNCTIONS
# ---------------------------
def add_to_cart(product):
    st.session_state.cart.append(product)
    st.success(f"Added {product['name']} to cart!")

def show_cart():
    st.header("🛒 Your Cart")
    cart = st.session_state.cart
    
    if len(cart) == 0:
        st.info("Your cart is empty.")
        return
    
    total = 0
    for item in cart:
        st.write(f"**{item['name']}** - ₹{item['price']}")
        total += item["price"]

    st.success(f"### Total Amount: ₹{total}")

# ---------------------------
# PAGE NAVIGATION
# ---------------------------
menu = ["Home", "Products", "Cart", "Checkout"]
choice = st.sidebar.selectbox("Menu", menu)

# ---------------------------
# PAGE — HOME
# ---------------------------
if choice == "Home":
    st.title("🛍️ Welcome to Streamlit E-Commerce Store")
    st.write("A simple demo online shopping app built using Streamlit.")
    st.image("https://via.placeholder.com/800x300?text=E-Commerce+Banner")

# ---------------------------
# PAGE — PRODUCTS
# ---------------------------
elif choice == "Products":
    st.title("🛒 Products")

    cols = st.columns(3)
    for index, product in enumerate(products):
        with cols[index % 3]:
            st.image(product["img"])
            st.write(f"### {product['name']}")
            st.write(f"**Price:** ₹{product['price']}")
            if st.button(f"Add to Cart {product['id']}", key=product['id']):
                add_to_cart(product)

# ---------------------------
# PAGE — CART
# ---------------------------
elif choice == "Cart":
    show_cart()

# ---------------------------
# PAGE — CHECKOUT
# ---------------------------
elif choice == "Checkout":
    st.title("💳 Checkout")
    if len(st.session_state.cart) == 0:
        st.info("Add items to your cart before checkout.")
    else:
        show_cart()
        st.success("Proceed to Payment (Dummy Page)")
        st.button("Pay Now")
