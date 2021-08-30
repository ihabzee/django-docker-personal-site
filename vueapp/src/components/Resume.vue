<template>
  <div>
    <b-container class="mt-4">
      <div v-for="section in sections" :key="section.id">
        <p v-html="section.content"></p>
      </div>
  </b-container>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Resume",
  data() {
    return {
      sections: [],
      type:[
        'Global',
        'Personal',
        'Experiance',
        'Education',
        'Other'
      ]
    };
  },
  methods: {
    prepareComponent: function () {
      axios
        .get("/api/sections/", {
          headers: {
            "Content-type": "application/json",
          },
        })
        .then((response) => {
          this.sections = response.data;
        });
    },
  },
  mounted() {
    this.prepareComponent();
  },
};
</script>
