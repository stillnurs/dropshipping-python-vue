<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <span class="button-box">
          <router-link to="/" class="navbar-item"
            ><strong>Drop-Ship</strong></router-link
          ></span
        >

        <a
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbar-menu"
          @click="showMobileMenu = !showMobileMenu"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div
        class="navbar-menu"
        id="navbar-menu"
        v-bind:class="{ 'is-active': showMobileMenu }"
      >
        <div class="navbar-start">
          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input
                    type="text"
                    class="input"
                    placeholder="What are you looking for?"
                    name="query"
                  />
                </div>

                <div class="control">
                  <button class="button is-success">
                    <span class="icon">
                      <i class="fas fa-search"></i>
                    </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
        <!-- bootsnip menu bar -->
        <div class="container">
          <nav class="navbar navbar-inverse">
            <div class="collapse navbar-collapse js-navbar-collapse">
              <ul class="nav navbar-nav">
                <li class="dropdown mega-dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown"
                    >Category-1 <span class="caret"></span
                  ></a>
                  <ul class="dropdown-menu mega-dropdown-menu">
                    <li class="col-sm-3">
                      <ul>
                        <li class="dropdown-header">SubCategory</li>
                        <div
                          id="menCollection"
                          class="carousel slide"
                          data-ride="carousel"
                        >
                          <div class="carousel-inner">
                            <div class="item active">
                              <a href="#"
                                ><img
                                  src="http://placehold.it/254x150/ff3546/f5f5f5/&text=New+Collection"
                                  class="img-responsive"
                                  alt="product 1"
                              /></a>
                              <h4>
                                <small>Summer dress floral prints</small>
                              </h4>
                              <button class="btn btn-primary" type="button">
                                49,99 €
                              </button>
                              <button
                                href="#"
                                class="btn btn-default"
                                type="button"
                              >
                                <span class="glyphicon glyphicon-heart"></span>
                                Add to Wishlist
                              </button>
                            </div>
                            <!-- End Item -->
                            <div class="item">
                              <a href="#"
                                ><img
                                  src="http://placehold.it/254x150/3498db/f5f5f5/&text=New+Collection"
                                  class="img-responsive"
                                  alt="product 2"
                              /></a>
                              <h4>
                                <small>Gold sandals with shiny touch</small>
                              </h4>
                              <button class="btn btn-primary" type="button">
                                9,99 €
                              </button>
                              <button
                                href="#"
                                class="btn btn-default"
                                type="button"
                              >
                                <span class="glyphicon glyphicon-heart"></span>
                                Add to Wishlist
                              </button>
                            </div>
                            <!-- End Item -->
                            <div class="item">
                              <a href="#"
                                ><img
                                  src="http://placehold.it/254x150/2ecc71/f5f5f5/&text=New+Collection"
                                  class="img-responsive"
                                  alt="product 3"
                              /></a>
                              <h4><small>Denin jacket stamped</small></h4>
                              <button class="btn btn-primary" type="button">
                                49,99 €
                              </button>
                              <button
                                href="#"
                                class="btn btn-default"
                                type="button"
                              >
                                <span class="glyphicon glyphicon-heart"></span>
                                Add to Wishlist
                              </button>
                            </div>
                            <!-- End Item -->
                          </div>
                          <!-- End Carousel Inner -->
                          <!-- Controls -->
                          <a
                            class="left carousel-control"
                            href="#menCollection"
                            role="button"
                            data-slide="prev"
                          >
                            <span
                              class="glyphicon glyphicon-chevron-left"
                              aria-hidden="true"
                            ></span>
                            <span class="sr-only">Previous</span>
                          </a>
                          <a
                            class="right carousel-control"
                            href="#menCollection"
                            role="button"
                            data-slide="next"
                          >
                            <span
                              class="glyphicon glyphicon-chevron-right"
                              aria-hidden="true"
                            ></span>
                            <span class="sr-only">Next</span>
                          </a>
                        </div>
                        <!-- /.carousel -->
                        <li class="divider"></li>
                        <li>
                          <a href="#"
                            >View all Collection
                            <span
                              class="glyphicon glyphicon-chevron-right pull-right"
                            ></span
                          ></a>
                        </li>
                      </ul>
                    </li>
                    <li class="col-sm-3">
                      <ul>
                        <li class="dropdown-header">Features</li>
                        <li><a href="#">Auto Carousel</a></li>
                        <li><a href="#">Carousel Control</a></li>
                        <li><a href="#">Left & Right Navigation</a></li>
                        <li><a href="#">Four Columns Grid</a></li>
                        <li class="divider"></li>
                        <li class="dropdown-header">Fonts</li>
                        <li><a href="#">Glyphicon</a></li>
                        <li><a href="#">Google Fonts</a></li>
                      </ul>
                    </li>
                    <li class="col-sm-3">
                      <ul>
                        <li class="dropdown-header">Plus</li>
                        <li><a href="#">Navbar Inverse</a></li>
                        <li><a href="#">Pull Right Elements</a></li>
                        <li><a href="#">Coloured Headers</a></li>
                        <li><a href="#">Primary Buttons & Default</a></li>
                      </ul>
                    </li>
                    <li class="col-sm-3">
                      <ul>
                        <li class="dropdown-header">Much more</li>
                        <li><a href="#">Easy to Customize</a></li>
                        <li><a href="#">Calls to action</a></li>
                        <li><a href="#">Custom Fonts</a></li>
                        <li><a href="#">Slide down on Hover</a></li>
                      </ul>
                    </li>
                  </ul>
                </li>
                <li class="dropdown mega-dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown"
                    >Category-2 <span class="caret"></span
                  ></a>
                  <ul class="dropdown-menu mega-dropdown-menu">
                    <li class="col-sm-3">
                      <ul>
                        <li class="dropdown-header">Features</li>
                        <li><a href="#">Auto Carousel</a></li>
                        <li><a href="#">Carousel Control</a></li>
                        <li><a href="#">Left & Right Navigation</a></li>
                        <li><a href="#">Four Columns Grid</a></li>
                        <li class="divider"></li>
                        <li class="dropdown-header">Fonts</li>
                        <li><a href="#">Glyphicon</a></li>
                        <li><a href="#">Google Fonts</a></li>
                      </ul>
                    </li>
                    <li class="col-sm-3">
                      <ul>
                        <li class="dropdown-header">Plus</li>
                        <li><a href="#">Navbar Inverse</a></li>
                        <li><a href="#">Pull Right Elements</a></li>
                        <li><a href="#">Coloured Headers</a></li>
                        <li><a href="#">Primary Buttons & Default</a></li>
                      </ul>
                    </li>
                    <li class="col-sm-3">
                      <ul>
                        <li class="dropdown-header">Much more</li>
                        <li><a href="#">Easy to Customize</a></li>
                        <li><a href="#">Calls to action</a></li>
                        <li><a href="#">Custom Fonts</a></li>
                        <li><a href="#">Slide down on Hover</a></li>
                      </ul>
                    </li>
                    <li class="col-sm-3">
                      <ul>
                        <li class="dropdown-header">Women Collection</li>
                        <div
                          id="womenCollection"
                          class="carousel slide"
                          data-ride="carousel"
                        >
                          <div class="carousel-inner">
                            <div class="item active">
                              <a href="#"
                                ><img
                                  src="http://placehold.it/254x150/3498db/f5f5f5/&text=New+Collection"
                                  class="img-responsive"
                                  alt="product 1"
                              /></a>
                              <h4>
                                <small>Summer dress floral prints</small>
                              </h4>
                              <button class="btn btn-primary" type="button">
                                49,99 €
                              </button>
                              <button
                                href="#"
                                class="btn btn-default"
                                type="button"
                              >
                                <span class="glyphicon glyphicon-heart"></span>
                                Add to Wishlist
                              </button>
                            </div>
                            <!-- End Item -->
                            <div class="item">
                              <a href="#"
                                ><img
                                  src="http://placehold.it/254x150/ff3546/f5f5f5/&text=New+Collection"
                                  class="img-responsive"
                                  alt="product 2"
                              /></a>
                              <h4>
                                <small>Gold sandals with shiny touch</small>
                              </h4>
                              <button class="btn btn-primary" type="button">
                                9,99 €
                              </button>
                              <button
                                href="#"
                                class="btn btn-default"
                                type="button"
                              >
                                <span class="glyphicon glyphicon-heart"></span>
                                Add to Wishlist
                              </button>
                            </div>
                            <!-- End Item -->
                            <div class="item">
                              <a href="#"
                                ><img
                                  src="http://placehold.it/254x150/2ecc71/f5f5f5/&text=New+Collection"
                                  class="img-responsive"
                                  alt="product 3"
                              /></a>
                              <h4><small>Denin jacket stamped</small></h4>
                              <button class="btn btn-primary" type="button">
                                49,99 €
                              </button>
                              <button
                                href="#"
                                class="btn btn-default"
                                type="button"
                              >
                                <span class="glyphicon glyphicon-heart"></span>
                                Add to Wishlist
                              </button>
                            </div>
                            <!-- End Item -->
                          </div>
                          <!-- End Carousel Inner -->
                          <!-- Controls -->
                          <a
                            class="left carousel-control"
                            href="#womenCollection"
                            role="button"
                            data-slide="prev"
                          >
                            <span
                              class="glyphicon glyphicon-chevron-left"
                              aria-hidden="true"
                            ></span>
                            <span class="sr-only">Previous</span>
                          </a>
                          <a
                            class="right carousel-control"
                            href="#womenCollection"
                            role="button"
                            data-slide="next"
                          >
                            <span
                              class="glyphicon glyphicon-chevron-right"
                              aria-hidden="true"
                            ></span>
                            <span class="sr-only">Next</span>
                          </a>
                        </div>
                        <!-- /.carousel -->
                        <li class="divider"></li>
                        <li>
                          <a href="#"
                            >View all Collection
                            <span
                              class="glyphicon glyphicon-chevron-right pull-right"
                            ></span
                          ></a>
                        </li>
                      </ul>
                    </li>
                  </ul>
                </li>
              </ul>
              <div class="navbar-end">
                <div class="navbar-item">
                  <div class="buttons">
                    <template
                      v-if="$store.state.isAuthenticated"
                      class="button"
                      data-toggle="dropdown"
                      role="button"
                      aria-expanded="false"
                    >
                      <ul class="nav navbar-nav navbar-right">
                        <li class="dropdown">
                          <span class="button-box">
                            <router-link
                              to="/my-account"
                              class="button is-light"
                            >
                              My account
                            </router-link>
                          </span>
                          <ul class="dropdown-menu" role="menu">
                            <li><a href="#">Action</a></li>
                            <li><a href="#">Another action</a></li>
                            <li><a href="#">Something else here</a></li>
                            <li class="divider"></li>
                            <li><a href="#">Separated link</a></li>
                          </ul>
                        </li>
                      </ul>
                    </template>

                    <template v-else>
                      <router-link to="/log-in" class="button is-light"
                        >Log in</router-link
                      >
                    </template>

                    <router-link to="/cart" class="button is-success">
                      <span class="icon"
                        ><i class="fas fa-shopping-cart"></i
                      ></span>
                      <span>Cart ({{ cartTotalLength }})</span>
                    </router-link>
                  </div>
                </div>
              </div>
            </div>
            <!-- /.nav-collapse -->
          </nav>
        </div>

        <!-- ------- -->
      </div>
    </nav>

    <div
      class="is-loading-bar has-text-centered"
      v-bind:class="{ 'is-loading': $store.state.isLoading }"
    >
      <div class="lds-dual-ring"></div>
    </div>

    <section class="section">
      <router-view />
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2021</p>
    </footer>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: [],
      },
    };
  },
  beforeCreate() {
    this.$store.commit("initializeStore");

    const token = this.$store.state.token;

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
  mounted() {
    this.cart = this.$store.state.cart;
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0;

      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity;
      }

      return totalLength;
    },
  },
};

$(document).ready(function() {
  $(".dropdown").hover(
    function() {
      $(".dropdown-menu", this)
        .not(".in .dropdown-menu")
        .stop(true, true)
        .slideDown("400");
      $(this).toggleClass("open");
    },
    function() {
      $(".dropdown-menu", this)
        .not(".in .dropdown-menu")
        .stop(true, true)
        .slideUp("400");
      $(this).toggleClass("open");
    }
  );
});
</script>

<style lang="scss">
@import "../node_modules/bulma";

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}

// Drop-down category bar
span.button-box {
  position: relative;
}
li.dropdown {
  padding-right: 25px;
}
.navbar-inverse {
  border-color: transparent;
  margin-top: 5px;
  align-content: center;
}
.navbar-collapse {
  padding-left: 500px;
}
.buttons .button {
  margin-bottom: 0;
  position: relative;
}
.button {
  border-color: #000;
}
.container {
  height: auto;
  position: relative;
  top: 5px;
}
.mega-dropdown {
  position: static !important;
}
.mega-dropdown-menu {
  padding: 20px 0px;
  width: 100%;
  box-shadow: none;
  -webkit-box-shadow: none;
}
.mega-dropdown-menu > li > ul {
  padding: 0;
  margin: 0;
}
.mega-dropdown-menu > li > ul > li {
  list-style: none;
}
.mega-dropdown-menu > li > ul > li > a {
  display: block;
  color: #222;
  padding: 3px 5px;
}
.mega-dropdown-menu > li ul > li > a:hover,
.mega-dropdown-menu > li ul > li > a:focus {
  text-decoration: none;
}
.mega-dropdown-menu .dropdown-header {
  font-size: 18px;
  color: #ff3546;
  padding: 5px 60px 5px 5px;
  line-height: 30px;
}

.carousel-control {
  width: 30px;
  height: 30px;
  top: -35px;
}
.left.carousel-control {
  right: 30px;
  left: inherit;
}
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  font-size: 12px;
  background-color: #fff;
  line-height: 30px;
  text-shadow: none;
  color: #333;
  border: 1px solid #ddd;
}
</style>
