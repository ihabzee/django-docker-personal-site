<template>
  <div>
    <b-container class="mt-4">
      <div v-if="articles.length > 0">
        <div v-for="article in articles" :key="article.uuid">
          <b-card no-body class="overflow-hidden"  >
            <b-row no-gutters>
              <b-col md="4">
                <b-card-img
                  :src="article.image_url"
                  :alt="article.title"
                  class="rounded-0"
                ></b-card-img>
              </b-col>
              <b-col md="8">
                <b-card-body   :title="article.title">
                  <b-card-text>
                    {{article.description}}
                  </b-card-text>
                </b-card-body>
              </b-col>
            </b-row>
            <b-row><b-link :href="article.url" class="card-link">Read Full Article</b-link></b-row>
          </b-card>
        </div>
      </div>
      <!-- <div v-else>No Articles found</div> -->
    </b-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Article",
  data() {
    return {
      articles: [],
    };
  },
  methods: {
    prepareComponent: function () {
      
      axios
        .get("/api/articles/", {
          headers: {
            "Content-type": "application/json",
          },
        })
        .then((response) => { 
          this.articles = response.data;
        });
    },
  },
  mounted() {
    this.prepareComponent();
  },
};
</script>