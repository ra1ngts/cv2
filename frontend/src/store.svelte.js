// stateCtx
export const stateCtx = $state({
    profile: {},
    categories: [],
    skills: [],
    certificates: [],
    frontendSkills: [],
    backendSkills: [],
    experience: [],
    projects: [],
    form: {},
    contactsData: {
        name: '',
        subject: '',
        message: '',
        email: ''
    },
    isSubmitting: false,
    formErrors: {},
    touchedFields: {},
    toast: {
        show: false,
        message: '',
        type: 'success'
    },
    activeSection: 'about',
    sections: [
        { id: 'about', label: 'About' },
        { id: 'experience', label: 'Experience' },
        { id: 'projects', label: 'Projects' },
        { id: 'contacts', label: 'Contacts' },
    ]
})

export const contactsForm = (recaptcha_token = null) => {
  const form = new FormData();
  form.set('name', stateCtx.contactsData.name || '');
  form.set('subject', stateCtx.contactsData.subject || '');
  form.set('message', stateCtx.contactsData.message || '');
  form.set('email', stateCtx.contactsData.email || '');

  if (recaptcha_token) {
    form.set('recaptcha_token', recaptcha_token);
  }

  console.log('contactsForm has sent data:', Object.fromEntries(form.entries()));
  return form;
};