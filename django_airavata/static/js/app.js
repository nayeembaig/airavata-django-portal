var AiravataApp=webpackJsonpAiravataApp([1],Array(30).concat([function(t,e,n){function a(t){n(123)}var i=n(0)(n(65),n(141),a,null,null);t.exports=i.exports},function(t,e,n){var a=n(0)(n(68),n(135),null,null,null);t.exports=a.exports},,function(t,e,n){"use strict";var a=n(20),i=n.n(a),s=n(76),o=n.n(s),r=n(73),l=n.n(r);e.a={addIndex:function(t){for(var e=0;e<t.length;e++)t[e].index=e;return t},getCSRFToken:function(){var t=document.cookie.split(";").map(function(t){return t.trim()}).filter(function(t){return t.startsWith("csrftoken=")}).map(function(t){return t.split("=")[1]});return t?t[0]:null},post:function(t,e){var n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"application/json",a=this.getCSRFToken(),i=new Headers({"Content-Type":n});return null!=a&&i.set("X-CSRFToken",a),fetch(t,{method:"post",body:l()(e),headers:i,credentials:"same-origin"}).then(function(t){return t.ok?o.a.resolve(t.json()):o.a.reject(new Error(t.statusText))})},mapper:function(t,e){var n=i()({},t);return function t(e,n){if(!(null==e||void 0==e||e instanceof Boolean||e instanceof String))if(e instanceof Array)for(var a in e)t(e[a],n);else if(e instanceof Object)for(var i in e){var s=i,o=e[i];t(o,n),n.hasOwnProperty(i)&&(s=n[i],delete e[i],e[s]=o)}}(n,e),n}}},,,,,,,,,,,,,,,,function(t,e,n){var a=n(0)(n(58),n(137),null,null,null);t.exports=a.exports},function(t,e,n){function a(t){n(124)}var i=n(0)(n(61),n(142),a,null,null);t.exports=i.exports},function(t,e,n){function a(t){n(125)}var i=n(0)(n(63),n(143),a,null,null);t.exports=i.exports},function(t,e,n){function a(t){n(126)}var i=n(0)(n(66),n(144),a,null,null);t.exports=i.exports},function(t,e,n){function a(t){n(122)}var i=n(0)(null,n(139),a,null,null);t.exports=i.exports},function(t,e,n){"use strict";var a=n(132),i=n.n(a),s=n(52),o=n.n(s),r=n(31),l=n.n(r),p=n(50),u=n.n(p),c=n(51),d=n.n(c),v=n(129),m=n.n(v),f=n(32),_=[{path:"/new/application",component:o.a,name:"newapp",children:[{path:"details",component:u.a,name:"details"},{path:"interface",component:d.a,name:"interface"},{path:"deployments",component:m.a,name:"deployments"}]},{path:"/",component:i.a},{path:"/experiments",component:l.a}];e.a=new f.a({routes:_})},function(t,e,n){"use strict";var a=n(7),i=n(8),s=n(71),o=n(72),r=n(70);i.a.use(a.a);var l={modules:{appInterfaceTab:o.a,appDetailsTab:s.a,appDeploymentsTab:r.a}};e.a=new a.a.Store(l)},function(t,e,n){var a=n(0)(null,n(140),null,null,null);t.exports=a.exports},,function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default={name:"dashboard-item",props:["dashboard_item","tags","height"],data:function(){return{height:100}}}},function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default={name:"recent-experiment",props:["experiment"]}},function(t,e){},function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=n(9),i=n.n(a),s=n(53),o=n.n(s),r=n(7),l=n.i(r.b)("appDetailsTab"),p=l.mapGetters,u=l.mapActions;e.default={components:{NewApplicationButtons:o.a},mounted:function(){this.syncDataFromStore()},data:function(){return{name:"",version:"",description:""}},methods:i()({syncDataFromStore:function(){this.name=this.getAppName(),this.version=this.getAppVersion(),this.description=this.getAppDescription()},updateStore:function(t,e){var n={};n[t]=e,this.updateAppDetails(n)}},p(["getAppName","getAppVersion","getAppDescription"]),u(["updateAppDetails","registerAppModule"])),watch:{name:function(t){this.updateStore("name",t)},version:function(t){this.updateStore("version",t)},description:function(t){this.updateStore("description",t)}}}},function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=n(9),i=n.n(a),s=n(30),o=n.n(s),r=n(7),l=n.i(r.b)("appInterfaceTab"),p=l.mapGetters,u=l.mapActions;e.default={components:{BooleanRadioButton:o.a},created:function(){this.syncDataFromStore()},methods:i()({delete_event_trigger:function(){this.$emit("delete_input_field")},boolValueHandler:function(t,e){if(console.log("Event Capture",t,e),"boolean"!=typeof e)throw"event value not boolean: ";this.updateStore(t,e)},syncDataFromStore:function(){console.log(this.input_id);var t=this.getAppInputField(this.input_id);this.name=t.name,this.value=t.value,this.type=t.type,this.appArg=t.appArg,this.userFriendlyDescr=t.userFriendlyDescr,this.inpOrder=t.inpOrder},updateStore:function(t,e){var n={id:this.input_id},a={};a[t]=e,n.update=a,this.updateInputFieldValues(n)}},u(["updateInputFieldValues"])),mounted:function(){this.syncDataFromStore()},data:function(){return{dataStaged:{id:this.input_id,fieldName:"dataStaged"},required:{id:this.input_id,fieldName:"required"},requiredOnCmd:{id:this.input_id,fieldName:"requiredOnCmd"},standardInput:{id:this.input_id,fieldName:"standardInput"},isReadOnly:{id:this.input_id,fieldName:"isReadOnly"},name:"",value:"",type:"",appArg:"",userFriendlyDescr:"",inpOrder:""}},props:["input_id"],computed:i()({},p(["getAppInputField","getAppInputFieldValue"])),watch:{inpOrder:function(t){this.updateStore("inpOrder",t)},userFriendlyDescr:function(t){this.updateStore("userFriendlyDescr",t)},name:function(t){this.updateStore("name",t)},value:function(t){this.updateStore("value",t)},type:function(t){this.updateStore("type",t)},appArg:function(t){this.updateStore("appArg",t)}}}},function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=n(9),i=n.n(a),s=n(130),o=n.n(s),r=n(30),l=n.n(r),p=n(53),u=n.n(p),c=n(131),d=n.n(c),v=n(7),m=n.i(v.b)("appInterfaceTab"),f=m.mapGetters,_=m.mapActions;e.default={components:{ApplicationInputField:o.a,BooleanRadioButton:l.a,NewApplicationButtons:u.a,ApplicationOutputField:d.a},data:function(){return{id:0,work_dir:{boolValue:!1},optional_files:{boolValue:!0},booleanSelectorIDs:["enableArchiveWorkingDirectory","enableOutputFileInputs"]}},props:{},mounted:function(){if(!this.isInitialized){var t=this.createAppInterfaceInputField(),e=this.createAppInterfaceOutputField();console.log("Mounted",t,e),this.initialized(!0),this.work_dir={boolValue:this.isEnableArchiveWorkingDirectory.toString()},this.optional_files={boolValue:this.isEnableOutputFileInput().toString()}}},computed:i()({},f(["getAppInputFieldsIds","getAppOutputFieldIds","isInitialized","isEnableArchiveWorkingDirectory","isEnableOutputFileInput"])),methods:i()({updateStore:function(t,e){t==this.booleanSelectorIDs[0]?this.changeEnableArchiveWorkingDirectory(e):t==this.booleanSelectorIDs[1]&&(this.changeEnableOutputFileInput(e),console.log(t))}},_(["createAppInterfaceInputField","deleteAppInterfaceInputField","createAppInterfaceOutputField","deleteAppInterfaceOutputField","initialized","changeEnableOutputFileInput","changeEnableArchiveWorkingDirectory"]))}},function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=n(9),i=n.n(a),s=n(30),o=n.n(s),r=n(7),l=n.i(r.b)("appInterfaceTab"),p=l.mapGetters,u=l.mapActions;e.default={components:{BooleanRadioButton:o.a},created:function(){this.syncDataFromStore()},props:["output_id"],methods:i()({delete_event_trigger:function(){this.$emit("delete_output_field")},boolValueHandler:function(t,e){console.log("Event Capture",t,e),this.updateStore(t,e)},syncDataFromStore:function(){console.log(this.output_id);var t=this.getAppOutputField(this.output_id);this.name=t.name,this.value=t.value,this.type=t.type,this.appArg=t.appArg},updateStore:function(t,e){var n={id:this.output_id},a={};a[t]=e,n.update=a,this.updateOutputField(n)}},u(["updateOutputField"])),mounted:function(){this.syncDataFromStore()},data:function(){return{required:"required",requiredOnCmd:"requiredOnCmd",dataMovement:"dataMovement",name:"",value:"",type:"",appArg:""}},computed:i()({},p(["getAppOutputField"])),watch:{inpOrder:function(t){this.updateStore("inpOrder",t)},userFriendlyDescr:function(t){this.updateStore("userFriendlyDescr",t)},name:function(t){this.updateStore("name",t)},value:function(t){this.updateStore("value",t)},type:function(t){this.updateStore("type",t)},appArg:function(t){this.updateStore("appArg",t)}}}},function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default={created:function(){this.boolValue=null!=this.def?this.def.toString():null},data:function(){return{boolValue:"false"}},props:{def:{type:Boolean,default:function(){return!1}},heading:{type:String},selectorId:{type:String,default:""}},methods:{triggerValueChangeEvent:function(t){this.selectorId;console.log("Triggered Change event"),this.$emit("bool_selector",this.selectorId,"true"==t)}},watch:{boolValue:function(t){this.triggerValueChangeEvent(t)}}}},function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=n(9),i=n.n(a),s=n(50),o=n.n(s),r=n(51),l=n.n(r),p=n(7),u=n.i(p.b)("appInterfaceTab"),c=u.mapActions;e.default={components:{ApplicationDetails:o.a,ApplicationInterface:l.a},mounted:function(){this.current_active_tab=this.$route.name,this.previous_active_tab=""},data:function(){return{current_active_tab:0,previous_active_tab:-1,appInterfaceTabData:{inputFields:[]}}},computed:{tabs:function(){var t={details:"",interface:"",deployments:""};return t[this.current_active_tab]="active",t.hasOwnProperty(this.previous_active_tab)&&(t[this.previous_active_tab]=""),t}},watch:{$route:function(t,e){this.tabs.hasOwnProperty(t.name)||this.initialize(!1),this.previous_active_tab=e.name,this.current_active_tab=t.name}},methods:i()({},c(["initialized"]))}},function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=n(49),i=n.n(a),s=n(52),o=n.n(s);e.default={data:function(){return{applications:[]}},components:{DashboardItem:i.a,NewApplication:o.a},mounted:function(){this.fetchApplications()},methods:{fetchApplications:function(){var t=this;this.$http.get("/api/applications").then(function(e){t.applications=e.body},function(e){t.applications=[{appModuleId:"",appModuleName:"No Applications Found",appModuleDescription:"",appModuleVersion:""}]})}}}},function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=n(49),i=n.n(a),s=n(128),o=n.n(s),r=n(33);e.default={name:"main-section",components:{DashboardItem:i.a,RecentExperiment:o.a},data:function(){var t={view_all:!1,default_experiment_count:3,height:180,applications:[],experiments:[{name:"Gaussian",description:"My very first test experiment",status:"Failed",updated:"14 minutes ago"},{name:"Lampps",description:"A really BIG experiment That Has a Really Long Title",status:"Completed",updated:"20 hours ago"},{name:"Gromacs",description:"exp_4a56w4892s23r6p9y_1",status:"Created",updated:"2 days ago"},{name:"RandExpr",description:"exp_4a56w4892s23r6p9y_1",status:"Failed",updated:"5 days ago"}]};return r.a.addIndex(t.experiments),t},mounted:function(){this.fetchApplications()},methods:{views_all_click_handler:function(){this.view_all=!this.view_all},fetchApplications:function(){var t=this;this.$http.get("/api/applications").then(function(e){t.applications=e.body},function(e){t.applications=[{appModuleId:"",appModuleName:"No Applications Found",appModuleDescription:"",appModuleVersion:""}]})}}}},function(t,e,n){"use strict";function a(t){return new i.a({el:"#app",router:c.a,store:d.a,template:"<"+t+"/>",components:{ExperimentsDashboard:l.a,AdminDashboard:u.a}})}Object.defineProperty(e,"__esModule",{value:!0}),e.initializeApacheAiravataDashboard=a;var i=n(8),s=n(57),o=n(32),r=n(31),l=n.n(r),p=n(56),u=n.n(p),c=n(54),d=n(55);i.a.config.productionTip=!1,i.a.use(s.a),i.a.use(o.a)},function(t,e,n){"use strict";var a=n(8);e.a={state:{app_module:"",app_compute_host:"",app_exec_path:"",app_parall_type:"",app_deployment_descr:""},mutations:{updateAppDeploymentValues:function(t,e){for(var n in e)t.hasOwnProperty(n)&&a.a.set(t,n,e[n])}},getters:{getAppModule:function(t){return t.app_module},getAppComputeHost:function(t){return t.app_compute_host},getAppExecutablePath:function(t){return t.app_exec_path},getAppParallelismType:function(t){return t.app_parall_type},getAppDeploymentDescription:function(t){return t.app_deployment_descr}},actions:{updateAppDeployment:function(t,e){t.commit("updateAppDeploymentValues",e)}}}},function(t,e,n){"use strict";var a=n(8),i=n(33);e.a={namespaced:!0,state:{name:"",version:"",description:""},mutations:{addAppDetails:function(t,e){for(var n in e)t.hasOwnProperty(n)&&a.a.set(t,n,e[n])},registerAppDetails:function(t){return i.a.post("/api/new/application/module",t)}},getters:{getAppName:function(t){return t.name},getAppVersion:function(t){return t.version},getAppDescription:function(t){return t.description},getAppDetails:function(t){return t}},actions:{updateAppDetails:function(t,e){t.commit("addAppDetails",e)},registerAppModule:function(t){t.commit("registerAppDetails")}}}},function(t,e,n){"use strict";var a=n(74),i=n.n(a),s=n(75),o=n.n(s),r=n(20),l=n.n(r),p=n(8);e.a={namespaced:!0,state:{inputFields:{},outputFields:{},counter:0,initialized:!1,enableArchiveWorkingDirectory:!1,enableOutputFileInputs:!1,missingFields:!1},mutations:{createAppInterfaceInputFieldObject:function(t,e){p.a.set(t.inputFields,e,{input_id:e,name:"nm",value:"",type:"",appArg:"",userFriendlyDescr:"",inpOrder:"",dataStaged:null,required:!1,requiredOnCmd:!1,isReadOnly:!0,standardInput:!0})},createAppInterfaceOutputFieldObject:function(t,e){p.a.set(t.outputFields,e,{input_id:e,name:"nm",value:"",type:"",appArg:"",required:!1,requiredOnCmd:!1,dataMovement:!0})},updateAppInterfaceField:function(t,e){var n=e.id,a=e.update,i=l()({},t[e.fieldType]);console.log(i);var s=i[n],r=o()(a);console.log("keys",r);for(var u in a)console.log("props",u),s.hasOwnProperty(u)&&(s[u]=a[u]);p.a.set(t,e.fieldType,i)},setInitialize:function(t,e){t.initialized=e},removeAppInterfaceField:function(t,e){var n=t[e.fieldType];delete n[e.id],p.a.set(t,e.fieldType,l()({},n))},deleteAllFields:function(t,e){p.a.set(t,e,{})},setEnableArchiveWorkingDirectory:function(t,e){t.enableArchiveWorkingDirectory=e},setEnableOutputFileInput:function(t,e){t.enableOutputFileInputs=e},setMissingField:function(t,e){t.missingFields=e}},getters:{isMissing:function(t){return t.missingFields},getAppInputField:function(t){return function(e){return t.inputFields[e]}},getAppOutputField:function(t){return function(e){return t.outputFields[e]}},isInitialized:function(t){return t.initialized},getAppInputFieldValue:function(t){return function(e){return t.inputFields[e.id][e.fieldName]}},getAppOutputFieldValue:function(t){return function(e){return t.outputFields[e.id][e.fieldName]}},isEnableArchiveWorkingDirectory:function(t){return t.enableArchiveWorkingDirectory},isEnableOutputFileInput:function(t){return t.enableOutputFileInputs},getAppInputFields:function(t){return t.inputFields},getAppOutputFields:function(t){return t.outputFields},getAppInputFieldsIds:function(t){var e=i()(t.inputFields);return e.splice(e.indexOf("__ob__"),1),e},getAppOutputFieldIds:function(t){var e=i()(t.outputFields);return e.splice(e.indexOf("__ob__"),1),e}},actions:{createAppInterfaceInputField:function(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:null;return null!=e&&t.state.inputFields.hasOwnProperty(e)||(e=(t.state.counter++).toString(),t.commit("createAppInterfaceInputFieldObject",e)),e},createAppInterfaceOutputField:function(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:null;return null!=e&&t.state.inputFields.hasOwnProperty(e)||(e=(t.state.counter++).toString(),t.commit("createAppInterfaceOutputFieldObject",e)),e},deleteAppInterfaceInputField:function(t,e){t.commit("removeAppInterfaceField",{fieldType:"inputFields",id:e})},deleteAppInterfaceOutputField:function(t,e){t.commit("removeAppInterfaceField",{fieldType:"outputFields",id:e})},updateInputFieldValues:function(t,e){e.fieldType="inputFields",t.commit("updateAppInterfaceField",e)},updateOutputField:function(t,e){e.fieldType="outputFields",t.commit("updateAppInterfaceField",e)},initialized:function(t,e){t.commit("setInitialize",e)},changeEnableOutputFileInput:function(t,e){t.commit("setEnableOutputFileInput",e)},changeEnableArchiveWorkingDirectory:function(t,e){t.commit("setEnableArchiveWorkingDirectory",e)},triggerMissingField:function(t,e){t.commit("setMissingField",e)}}}},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,function(t,e){},function(t,e){},function(t,e){},function(t,e){},function(t,e){},function(t,e){},function(t,e){},function(t,e){},function(t,e){},function(t,e,n){var a=n(0)(n(59),n(136),null,null,null);t.exports=a.exports},function(t,e,n){function a(t){n(127)}var i=n(0)(n(60),n(145),a,null,null);t.exports=i.exports},function(t,e,n){function a(t){n(119)}var i=n(0)(n(62),n(133),a,null,null);t.exports=i.exports},function(t,e,n){function a(t){n(121)}var i=n(0)(n(64),n(138),a,null,null);t.exports=i.exports},function(t,e,n){function a(t){n(120)}var i=n(0)(n(67),n(134),a,null,null);t.exports=i.exports},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"main_section interface-main"},[n("div",{staticClass:"input-field-header"},[t._v("\n    Input Fields\n    "),n("img",{attrs:{src:"/static/images/delete.png"},on:{click:function(e){t.delete_event_trigger()}}})]),t._v(" "),n("div",{staticClass:"entry"},[n("div",{staticClass:"heading"},[t._v("Name")]),t._v(" "),n("input",{directives:[{name:"model",rawName:"v-model",value:t.name,expression:"name"}],attrs:{type:"text"},domProps:{value:t.name},on:{input:function(e){e.target.composing||(t.name=e.target.value)}}})]),t._v(" "),n("div",{staticClass:"entry"},[n("div",{staticClass:"heading"},[t._v("Value")]),t._v(" "),n("input",{directives:[{name:"model",rawName:"v-model",value:t.value,expression:"value"}],attrs:{type:"text"},domProps:{value:t.value},on:{input:function(e){e.target.composing||(t.value=e.target.value)}}})]),t._v(" "),n("div",{staticClass:"entry"},[n("div",{staticClass:"heading"},[t._v("Type")]),t._v(" "),n("select",{directives:[{name:"model",rawName:"v-model",value:t.type,expression:"type"}],on:{change:function(e){var n=Array.prototype.filter.call(e.target.options,function(t){return t.selected}).map(function(t){return"_value"in t?t._value:t.value});t.type=e.target.multiple?n:n[0]}}},[n("option",{attrs:{value:"String"}},[t._v("String")]),t._v(" "),n("option",{attrs:{value:"Integer"}},[t._v("Integer")]),t._v(" "),n("option",{attrs:{value:"Float"}},[t._v("Float")]),t._v(" "),n("option",{attrs:{value:"URI"}},[t._v("URI")])])]),t._v(" "),n("div",{staticClass:"entry"},[n("div",{staticClass:"heading"},[t._v("Application argument")]),t._v(" "),n("input",{directives:[{name:"model",rawName:"v-model",value:t.appArg,expression:"appArg"}],attrs:{type:"text"},domProps:{value:t.appArg},on:{input:function(e){e.target.composing||(t.appArg=e.target.value)}}})]),t._v(" "),n("div",{staticClass:"entry boolean-selectors"},[n("boolean-radio-button",{attrs:{heading:"Standard input",selectorId:t.standardInput.fieldType,def:t.getAppInputFieldValue(t.standardInput)},on:{bool_selector:t.boolValueHandler}}),t._v(" "),n("boolean-radio-button",{attrs:{heading:"Is read only",selectorId:t.isReadOnly.fieldType,def:t.getAppInputFieldValue(t.isReadOnly)},on:{bool_selector:t.boolValueHandler}})],1),t._v(" "),n("div",{staticClass:"entry"},[n("div",{staticClass:"heading"},[t._v("User friendly description")]),t._v(" "),n("textarea",{directives:[{name:"model",rawName:"v-model",value:t.userFriendlyDescr,expression:"userFriendlyDescr"}],staticStyle:{height:"80px"},attrs:{type:"text"},domProps:{value:t.userFriendlyDescr},on:{input:function(e){e.target.composing||(t.userFriendlyDescr=e.target.value)}}})]),t._v(" "),n("div",{staticClass:"entry"},[n("div",{staticClass:"heading"},[t._v("Input order")]),t._v(" "),n("input",{directives:[{name:"model",rawName:"v-model",value:t.inpOrder,expression:"inpOrder"}],attrs:{type:"text"},domProps:{value:t.inpOrder},on:{input:function(e){e.target.composing||(t.inpOrder=e.target.value)}}})]),t._v(" "),n("div",{staticClass:"entry boolean-selectors"},[n("boolean-radio-button",{attrs:{heading:"Data is staged",selectorId:t.dataStaged.fieldType,def:t.getAppInputFieldValue(t.dataStaged)},on:{bool_selector:t.boolValueHandler}}),t._v(" "),n("boolean-radio-button",{attrs:{heading:"Required",selectorId:t.required.fieldType,def:t.getAppInputFieldValue(t.required)},on:{bool_selector:t.boolValueHandler}})],1),t._v(" "),n("div",{staticClass:"entry boolean-selectors"},[n("boolean-radio-button",{attrs:{heading:"Required on command line",selectorId:t.requiredOnCmd.fieldType},on:{bool_selector:t.boolValueHandler}})],1)])},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"new_app"},[n("div",{staticClass:"new_app_header"},[n("h4",{staticStyle:{display:"inline-block"}},[t._v("Application Catalog")]),t._v(" "),n("router-link",{attrs:{to:{name:"details"}}},[n("button",t._g({},this.$emit("new_application")),[t._v("New Application "),n("span",[t._v("+")])])])],1),t._v(" "),n("div",{staticClass:"applications"},[n("h6",{staticStyle:{color:"#666666"}},[t._v("APPLICATIONS")]),t._v(" "),n("div",{staticClass:"container-fluid"},[n("div",{staticClass:"row"},t._l(t.applications,function(t){return n("DashboardItem",{key:t.title,attrs:{dashboard_item:t}})}))])])])},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"stage"},[n("main",{staticClass:"main-content"},[t._m(0),t._v(" "),n("div",{staticClass:"container-fluid"},[n("div",{staticClass:"row"},t._l(t.applications,function(e){return n("DashboardItem",{key:e.title,attrs:{dashboard_item:e,height:t.height}})}))])]),t._v(" "),n("aside",{staticClass:"sidebar"},[n("header",{staticClass:"sidebar-header"},[n("h1",{staticClass:"sidebar-header__title"},[t._v("Recent Experiments")]),t._v(" "),n("a",{staticClass:"sidebar-header__action",attrs:{href:"#0"},on:{click:t.views_all_click_handler}},[t._v("View all")])]),t._v(" "),n("ol",{staticClass:"feed"},t._l(t.experiments,function(e){return e.index<t.default_experiment_count||t.view_all?n("RecentExperiment",{key:e.name,attrs:{experiment:e}}):t._e()}))])])},staticRenderFns:[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"container-fluid"},[n("h1",{staticClass:"h4 mb-4"},[t._v("Dashboard")])])}]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("li",{staticClass:"feed__list-item"},[n("span",{staticClass:"feed__label text-secondary"},[t._v(t._s(t.experiment.name))]),t._v(" "),n("h2",{staticClass:"feed__title mb-2"},[n("a",{attrs:{href:"#0"}},[t._v(t._s(t.experiment.description))])]),t._v(" "),"Completed"==t.experiment.status?n("span",{staticClass:"badge badge-success"},[t._v(t._s(t.experiment.status))]):"Created"==t.experiment.status?n("span",{staticClass:"badge badge-primary"},[t._v(t._s(t.experiment.status))]):n("span",{staticClass:"badge badge-danger"},[t._v(t._s(t.experiment.status))]),t._v(" "),n("div",{staticClass:"feed__item-meta text-secondary mt-1"},[n("span",[t._v("Updated")]),t._v(" "),n("time",[t._v(t._s(t.experiment.updated))])])])},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"col-md-6 col-xl-4"},[n("div",{staticClass:"card"},[n("a",{staticClass:"card-link text-dark",style:"min-height:"+t.height+"px;",attrs:{href:"#0"}},[n("div",{staticClass:"card-body"},[n("h2",{staticClass:"card-title h5"},[t._v(t._s(t.dashboard_item.appModuleName))]),t._v(" "),t._l(t.dashboard_item.tags,function(e){return n("span",{staticClass:"badge badge-primary mr-1"},[t._v(t._s(e))])}),t._v(" "),t.dashboard_item.appModuleVersion?n("span",{staticClass:"badge badge-primary mr-1"},[t._v(t._s(t.dashboard_item.appModuleVersion))]):t._e(),t._v(" "),n("p",{staticClass:"card-text card-text--small mt-3 text-secondary"},[t._v(t._s(t.dashboard_item.appModuleDescription))])],2)])])])},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"main_section interface-main"},[n("div",{staticClass:"input-field-header"},[t._v("\n    Output Fields\n    "),n("img",{attrs:{src:"/static/images/delete.png"},on:{click:function(e){t.delete_event_trigger()}}})]),t._v(" "),n("div",{staticClass:"entry"},[n("div",{staticClass:"heading"},[t._v("Name")]),t._v(" "),n("input",{directives:[{name:"model",rawName:"v-model",value:t.name,expression:"name"}],attrs:{type:"text"},domProps:{value:t.name},on:{input:function(e){e.target.composing||(t.name=e.target.value)}}})]),t._v(" "),n("div",{staticClass:"entry"},[n("div",{staticClass:"heading"},[t._v("Value")]),t._v(" "),n("input",{directives:[{name:"model",rawName:"v-model",value:t.value,expression:"value"}],attrs:{type:"text"},domProps:{value:t.value},on:{input:function(e){e.target.composing||(t.value=e.target.value)}}})]),t._v(" "),n("div",{staticClass:"entry"},[n("div",{staticClass:"heading"},[t._v("Type")]),t._v(" "),n("select",{directives:[{name:"model",rawName:"v-model",value:t.type,expression:"type"}],on:{change:function(e){var n=Array.prototype.filter.call(e.target.options,function(t){return t.selected}).map(function(t){return"_value"in t?t._value:t.value});t.type=e.target.multiple?n:n[0]}}},[n("option",{attrs:{value:"String"}},[t._v("String")]),t._v(" "),n("option",{attrs:{value:"Integer"}},[t._v("Integer")]),t._v(" "),n("option",{attrs:{value:"Float"}},[t._v("Float")]),t._v(" "),n("option",{attrs:{value:"URI"}},[t._v("URI")])])]),t._v(" "),n("div",{staticClass:"entry"},[n("div",{staticClass:"heading"},[t._v("Application argument")]),t._v(" "),n("input",{directives:[{name:"model",rawName:"v-model",value:t.appArg,expression:"appArg"}],attrs:{type:"text"},domProps:{value:t.appArg},on:{input:function(e){e.target.composing||(t.appArg=e.target.value)}}})]),t._v(" "),n("div",{staticClass:"entry boolean-selectors"},[n("boolean-radio-button",{attrs:{heading:"Data Movement",selectorId:t.dataMovement},on:{bool_selector:t.boolValueHandler}}),t._v(" "),n("boolean-radio-button",{attrs:{heading:"Output Required",selectorId:t.required},on:{bool_selector:t.boolValueHandler}})],1),t._v(" "),n("div",{staticClass:"entry boolean-selectors"},[n("boolean-radio-button",{attrs:{heading:"Required on command line",selectorId:t.requiredOnCmd},on:{bool_selector:t.boolValueHandler}})],1)])},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"btns"},[n("input",{staticClass:"cancel",attrs:{type:"button",value:"Cancel"},on:{click:function(e){t.$emit("cancel")}}}),t._v(" "),n("input",{staticClass:"save",attrs:{type:"button",value:"Save"},on:{click:function(e){t.$emit("save")}}})])},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement;return(t._self._c||e)("router-view")},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"boolean-selector-main"},[n("div",{staticClass:"boolean-selector-heading"},[t._v(t._s(t.heading))]),t._v(" "),n("div",{staticClass:"boolean-selector"},[n("div",[n("input",{directives:[{name:"model",rawName:"v-model",value:t.boolValue,expression:"boolValue"}],attrs:{type:"radio",value:"true"},domProps:{checked:t._q(t.boolValue,"true")},on:{__c:function(e){t.boolValue="true"}}}),t._v(" "),n("label",[t._v("True")])]),t._v(" "),n("div",[n("input",{directives:[{name:"model",rawName:"v-model",value:t.boolValue,expression:"boolValue"}],attrs:{type:"radio",value:"false"},domProps:{checked:t._q(t.boolValue,"false")},on:{__c:function(e){t.boolValue="false"}}}),t._v(" "),n("label",[t._v("False")])])])])},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"main_section"},[n("div",{staticClass:"new-application-tab-main"},[n("h4",[t._v("Application Details")]),t._v(" "),n("div",{staticClass:"entry"},[n("div",{staticClass:"heading"},[t._v("Application Name")]),t._v(" "),n("input",{directives:[{name:"model",rawName:"v-model",value:t.name,expression:"name"}],attrs:{type:"text"},domProps:{value:t.name},on:{input:function(e){e.target.composing||(t.name=e.target.value)}}})]),t._v(" "),n("div",{staticClass:"entry"},[n("div",{staticClass:"heading"},[t._v("Application Version")]),t._v(" "),n("input",{directives:[{name:"model",rawName:"v-model",value:t.version,expression:"version"}],attrs:{type:"text"},domProps:{value:t.version},on:{input:function(e){e.target.composing||(t.version=e.target.value)}}})]),t._v(" "),n("div",{staticClass:"entry"},[n("div",{staticClass:"heading"},[t._v("Experiment Description")]),t._v(" "),n("textarea",{directives:[{name:"model",rawName:"v-model",value:t.description,expression:"description"}],staticStyle:{height:"80px"},attrs:{type:"text"},domProps:{value:t.description},on:{input:function(e){e.target.composing||(t.description=e.target.value)}}})]),t._v(" "),n("new-application-buttons",{on:{save:function(e){t.registerAppModule()}}})],1)])},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"main_section"},[n("div",{staticClass:"new-application-tab-main"},[n("h4",[t._v("Application Interface")]),t._v(" "),n("div",{staticClass:"entry boolean-selectors"},[n("boolean-radio-button",{attrs:{heading:"Enable Archiving Working Directory",selectorVal:t.work_dir,def:null,selectorId:t.booleanSelectorIDs[0]},on:{bool_selector:t.updateStore}}),t._v(" "),n("boolean-radio-button",{attrs:{heading:"Enable Optional File Inputs",selectorVal:t.optional_files,def:null,selectorId:t.booleanSelectorIDs[1]},on:{bool_selector:t.updateStore}})],1),t._v(" "),n("div",t._l(t.getAppInputFieldsIds,function(e){return n("application-input-field",{key:e,staticClass:"interface-main",attrs:{input_id:e},on:{delete_input_field:function(n){t.deleteAppInterfaceInputField(e)}}})})),t._v(" "),n("div",{staticClass:"entry"},[n("button",{staticClass:"interface-btn",on:{click:function(e){t.createAppInterfaceInputField()}}},[t._v("Add Application "),n("span",[t._v("input")])])]),t._v(" "),n("div",t._l(t.getAppOutputFieldIds,function(e){return n("application-output-field",{key:e,staticClass:"interface-main",attrs:{output_id:e},on:{delete_output_field:function(n){t.deleteAppInterfaceOutputField(e)}}})})),t._v(" "),n("div",{staticClass:"entry"},[n("div",{staticClass:"heading"},[t._v("Output fields")]),t._v(" "),n("button",{staticClass:"interface-btn",on:{click:function(e){t.createAppInterfaceOutputField()}}},[t._v("Add Application "),n("span",[t._v("output")])])]),t._v(" "),n("new-application-buttons")],1)])},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"new_app"},[n("h3",[t._v("Create A New Application")]),t._v(" "),n("div",{staticClass:"main"},[n("div",{staticClass:"tabs"},[n("div",{staticClass:"tab",class:t.tabs.details},[n("router-link",{staticClass:"link",attrs:{to:{name:"details"}}},[n("label",{staticClass:"lbl"},[t._v("Details")])])],1),t._v(" "),n("div",{staticClass:"tab",class:t.tabs.interface,attrs:{obj:t.appInterfaceTabData}},[n("router-link",{staticClass:"link",attrs:{to:{name:"interface"}}},[n("label",{staticClass:"lbl"},[t._v("Interface")])])],1),t._v(" "),n("div",{staticClass:"tab",class:t.tabs.deployments},[n("router-link",{staticClass:"link",attrs:{to:{name:"deployments"}}},[n("label",{staticClass:"lbl"},[t._v("Deployments")])])],1),t._v(" "),n("div",{staticClass:"tab",staticStyle:{width:"100%"}})]),t._v(" "),n("transition",{attrs:{mode:"out-in"}},[n("router-view",{key:t.$route.path})],1)],1)])},staticRenderFns:[]}},function(t,e){t.exports={render:function(){var t=this,e=t.$createElement;t._self._c;return t._m(0)},staticRenderFns:[function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"main_section"},[n("div",{staticClass:"new-application-tab-main"},[n("h4",[t._v("Application Deployments")]),t._v(" "),n("div",{staticClass:"entry"},[n("div",{staticClass:"heading"},[t._v("Application module")]),t._v(" "),n("input",{attrs:{type:"text"}})]),t._v(" "),n("div",{staticClass:"entry"},[n("div",{staticClass:"heading"},[t._v("Application compute host")]),t._v(" "),n("input",{attrs:{type:"text"}})]),t._v(" "),n("div",{staticClass:"entry"},[n("div",{staticClass:"heading"},[t._v("Application executable path")]),t._v(" "),n("input",{attrs:{type:"text"}})]),t._v(" "),n("div",{staticClass:"entry"},[n("div",{staticClass:"heading"},[t._v("Application Parallelism type")]),t._v(" "),n("input",{attrs:{type:"text"}})]),t._v(" "),n("div",{staticClass:"entry"},[n("div",{staticClass:"heading"},[t._v("Application deployment description")]),t._v(" "),n("textarea",{staticStyle:{height:"80px"},attrs:{type:"text"}})])]),t._v(" "),n("div",{staticClass:"new-application-tab-main"},[n("h4",[t._v("Module load commands")]),t._v(" "),n("div",{staticClass:"entry"},[n("div",{staticClass:"heading"},[t._v("Module load commands")]),t._v(" "),n("input",{attrs:{type:"text"}})]),t._v(" "),n("div",{staticClass:"deployment-entry"},[n("input",{staticClass:"deployment btn",attrs:{type:"button",value:"Add command"}})])]),t._v(" "),n("div",{staticClass:"new-application-tab-main"},[n("div",{staticClass:"deployment-entry"},[n("h4",[t._v("Library Prepend Paths")]),t._v(" "),n("input",{staticClass:"deployment btn",attrs:{type:"button",value:"Add path"}})])]),t._v(" "),n("div",{staticClass:"new-application-tab-main"},[n("div",{staticClass:"deployment-entry"},[n("h4",[t._v("Library Append Paths")]),t._v(" "),n("input",{staticClass:"deployment btn",attrs:{type:"button",value:"Add path"}})])]),t._v(" "),n("div",{staticClass:"new-application-tab-main"},[n("div",{staticClass:"deployment-entry"},[n("h4",[t._v("Environments")]),t._v(" "),n("input",{staticClass:"deployment btn",attrs:{type:"button",value:"Add environment"}})])]),t._v(" "),n("div",{staticClass:"new-application-tab-main"},[n("div",{staticClass:"deployment-entry"},[n("h4",[t._v("Pre Job Commands")]),t._v(" "),n("input",{staticClass:"deployment btn",attrs:{type:"button",value:"Add command"}})])]),t._v(" "),n("div",{staticClass:"new-application-tab-main"},[n("div",{staticClass:"deployment-entry"},[n("h4",[t._v("Post Job Commands")]),t._v(" "),n("input",{staticClass:"deployment btn",attrs:{type:"button",value:"Add command"}})])]),t._v(" "),n("div",{staticClass:"new-application-tab-main"},[n("div",{staticClass:"deployment-entry"},[n("h4",[t._v("Defaults")]),t._v(" "),n("input",{staticClass:"deployment btn",attrs:{type:"button",value:"Add command"}})])])])}]}},,,function(t,e){}]),[69]);
//# sourceMappingURL=app.js.map