<template>
  <div>
    <b-container>
      <b-alert v-if="showAlert" variant="alertVariant">{{alertMessage}}</b-alert>
      <b-form @submit="onSubmit" @reset="onReset">
        <b-form-group
          id="input-group-1"
          label="Email address:"
          label-for="email"
          description="I'll never share your email with anyone else."
          label-align="left"
          style="text-align: left"
        >
          <b-form-input
            id="email"
            v-model="form.email"
            type="email"
            placeholder="Enter email"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-2"
          label="Subject:"
          label-for="subject"
          style="text-align: left"
        >
          <b-form-input
            id="subject"
            v-model="form.subject"
            placeholder="Enter Subject"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-2"
          label="Content:"
          label-for="content"
          style="text-align: left"
        >
          <b-form-textarea
            id="content"
            v-model="form.content"
            placeholder="Message Content"
            rows="8"
          ></b-form-textarea>
        </b-form-group>
        <vue-recaptcha
          sitekey="6LdvqzIcAAAAABAuLpiEnPQOp28uAHLcKLWt_UOt"
          ref="invisibleRecaptcha"
          @verify="onVerify"
          @expired="onExpired"
          size="invisible"
        >
        </vue-recaptcha>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-container>
  </div>
</template>

<script>
import VueRecaptcha from "vue-recaptcha";
import axios from "axios";
export default {
  name: "ContactMe",
  components: {
    VueRecaptcha,
  },
  data() {
    return {
      canSubmit: true,
      showAlert: false,
      alertVariant: 'danger',
      alertMessage :'',
      form: {
        email: "",
        subject: "",
        content: "",
      },
    };
  },
  methods: {
    onVerify: function (response) {
      if (response == undefined || response == "") {
        this.canSubmit = false;
      }
    },
    onExpired: function () {
      console.log("Expired");
    },
    resetRecaptcha() {
      this.$refs.recaptcha.reset(); // Direct call reset method
    },
    onSubmit(event) {
      console.log(this.$refs.invisibleRecaptcha.execute());
      axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
      axios.defaults.xsrfCookieName = "csrftoken"
      axios
        .post("/api/contact-me/", this.form,{
          headers: {
            "Content-type": "application/json",
          },
        })
        .then((response) => {
          this.sections = response.data;
        });
        event.preventDefault();
    },
    onReset(event) {
      event.preventDefault();
      // Reset our form values
      this.form.email = "";
      this.form.subject = "";
      this.form.content = "";
    },
  },
};
</script> 