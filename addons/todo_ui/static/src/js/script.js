odoo.define('todo_ui.example_module', async require => {
  console.log('called')

  const Model = require('web.Model');


  const User = new Model('res.users');


  User.query([]).all().then((users) => {
    console.log('All Users', users);
  });


  // const users = await User.query([]).all();

  // console.log(users);
});


/*


async function someFunc() {

try {

  const users = await User.query().all()


} catch {

}

}


someFunc().then()


async function func2() {
  const res = await someFunc()
}


*/


odoo.define('todo_ui.widgets', function(require) {

  var common = require('web.form_common');
  const Widget = require('web.Widget');
  const core = require('web.core');

  // const ToggleButton = Widget.extend({

  // });


  const ToggleButton =  common.AbstractField.extend(common.CompletionFieldMixin, common.ReinitializeFieldMixin, {
    template: 'ToggleButton',
    // events: {
    //   'click .switch': 'on_switch_click',
    // },
    init(...args) {
      this._super(...args);

    },

    on_switch_click() {
      console.log('from events');
      this.set('value', this.$('input')[0].checked);
    },

    start() {


      // this.on('change:value', this, function() {
      //   console.log('value changed');
      // });
        this.$('input')[0].disabled = !!this.get('effective_readonly');

        this.on('change:effective_readonly', this, function() {
              this.$('input')[0].disabled = !!this.get('effective_readonly');
        });



      // this.get('')
      // console.log(this.get('value'))

      // if(this.get('value')) {
      //   this.$('input')[0].checked=true
      // }

      this.$('input')[0].checked=!!this.get('value');

      this.$el.on('click', () => {
        this.set('value', this.$('input')[0].checked);
      });
    },


    // renderElement(...args) {
    //   this._super(...args);


    //   if(this.get('effective_readonly')) {
    //     this.$('input')[0].disabled = true;
    //   }

    //    else {
    //     this.$('input')[0].disabled = false;
    //   }

    //   console.log('ren')
    // }
  });


  core.form_widget_registry.add("gbt_toggle_button", ToggleButton);

  return ToggleButton;
})
