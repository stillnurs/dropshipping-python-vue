<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"
          ><strong>Drop-Ship</strong></router-link
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

        <div class="navbar-end">
          <!-- Drop-down Category bar -->
          <nav class="navbar navbar-default navbar-static">
            <div class="navbar-header">
              <button
                class="navbar-toggle"
                type="button"
                data-toggle="collapse"
                data-target=".js-navbar-collapse"
              >
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="#">Large Dropdown Menu</a>
            </div>

            <div class="collapse navbar-collapse js-navbar-collapse">
              <ul class="nav navbar-nav">
                <li class="dropdown dropdown-large">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown"
                    >Dropdown <b class="caret"></b
                  ></a>

                  <ul class="dropdown-menu dropdown-menu-large row">
                    <li class="col-sm-3">
                      <ul>
                        <li class="dropdown-header">Glyphicons</li>
                        <li><a href="#">Available glyphs</a></li>
                        <li class="disabled"><a href="#">How to use</a></li>
                        <li><a href="#">Examples</a></li>
                        <li class="divider"></li>
                        <li class="dropdown-header">Dropdowns</li>
                        <li><a href="#">Example</a></li>
                        <li><a href="#">Aligninment options</a></li>
                        <li><a href="#">Headers</a></li>
                        <li><a href="#">Disabled menu items</a></li>
                      </ul>
                    </li>
                    <li class="col-sm-3">
                      <ul>
                        <li class="dropdown-header">Button groups</li>
                        <li><a href="#">Basic example</a></li>
                        <li><a href="#">Button toolbar</a></li>
                        <li><a href="#">Sizing</a></li>
                        <li><a href="#">Nesting</a></li>
                        <li><a href="#">Vertical variation</a></li>
                        <li class="divider"></li>
                        <li class="dropdown-header">Button dropdowns</li>
                        <li><a href="#">Single button dropdowns</a></li>
                      </ul>
                    </li>
                    <li class="col-sm-3">
                      <ul>
                        <li class="dropdown-header">Input groups</li>
                        <li><a href="#">Basic example</a></li>
                        <li><a href="#">Sizing</a></li>
                        <li><a href="#">Checkboxes and radio addons</a></li>
                        <li class="divider"></li>
                        <li class="dropdown-header">Navs</li>
                        <li><a href="#">Tabs</a></li>
                        <li><a href="#">Pills</a></li>
                        <li><a href="#">Justified</a></li>
                      </ul>
                    </li>
                    <li class="col-sm-3">
                      <ul>
                        <li class="dropdown-header">Navbar</li>
                        <li><a href="#">Default navbar</a></li>
                        <li><a href="#">Buttons</a></li>
                        <li><a href="#">Text</a></li>
                        <li><a href="#">Non-nav links</a></li>
                        <li><a href="#">Component alignment</a></li>
                        <li><a href="#">Fixed to top</a></li>
                        <li><a href="#">Fixed to bottom</a></li>
                        <li><a href="#">Static top</a></li>
                        <li><a href="#">Inverted navbar</a></li>
                      </ul>
                    </li>
                  </ul>
                </li>
              </ul>
            </div>
            <!-- /.nav-collapse -->
          </nav>

          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-light"
                  >My account</router-link
                >
              </template>

              <template v-else>
                <router-link to="/log-in" class="button is-light"
                  >Log in</router-link
                >
              </template>

              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart ({{ cartTotalLength }})</span>
              </router-link>
            </div>
          </div>
        </div>
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
.dropdown-large {
  position: static !important;
}
.dropdown-menu-large {
  /*margin-left: inherit;*/
  left: inherit;
  margin-right: 16px;
  padding: 20px 0px;
}
.dropdown-menu-large > li > ul {
  padding: 0;
  margin: 0;
}
.dropdown-menu-large > li > ul > li {
  list-style: none;
}
.dropdown-menu-large > li > ul > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.428571429;
  color: #333333;
  white-space: normal;
}
.dropdown-menu-large > li ul > li > a:hover,
.dropdown-menu-large > li ul > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu-large .disabled > a,
.dropdown-menu-large .disabled > a:hover,
.dropdown-menu-large .disabled > a:focus {
  color: #999999;
}
.dropdown-menu-large .disabled > a:hover,
.dropdown-menu-large .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.dropdown-menu-large .dropdown-header {
  color: #428bca;
  font-size: 18px;
}
@media (max-width: 768px) {
  .dropdown-menu-large {
    margin-left: 0;
    margin-right: 0;
  }
  .dropdown-menu-large > li {
    margin-bottom: 30px;
  }
  .dropdown-menu-large > li:last-child {
    margin-bottom: 0;
  }
  .dropdown-menu-large .dropdown-header {
    padding: 3px 15px !important;
  }
}
.navbar {
  border: none;
}
</style>
