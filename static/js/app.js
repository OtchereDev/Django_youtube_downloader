
const resolution = document.querySelector('.resolution')
const lower_limit = document.querySelector('.lower_limit')
const upper_limit = document.querySelector('.upper_limit')
const url_link = document.querySelector('.url_link')
const submit_btn = document.querySelector('.submit_btn')
const downloader_form = document.querySelector('.downloader_form')


// fetch action
async function postAPI(data){

    const response= await fetch('/download',{
        method: 'POST', 
        mode: 'cors', 
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data) // body data type must match "Content-Type" header
      });
    return response.json();
}


// functions 
function submitRequest(){
    const resolution_val = resolution.value
    const lower_limit_val = lower_limit.value
    const upper_limit_val = upper_limit.value
    const url_link_val = url_link.value

    // if(!lower_limit_val){
    //     lower_limit.style.borderColor = 'Red'
    //     console.log(lower_limit.style)

    // }else{
    //     lower_limit.style.borderColor = ''
    // }

    validateInput(resolution)
    validateInput(upper_limit)
    validateInput(lower_limit)
    validateInput(url_link)

    // if (resolution_val && lower_limit_val && upper_limit_val && url_link_val){

    // }else if (!resol) {
        
    // }

    console.log(resolution_val,
        lower_limit_val,
        upper_limit_val,
        url_link_val)
}


function validateInput(input_type){
    const resolution_val = resolution.value
    const lower_limit_val = lower_limit.value
    const upper_limit_val = upper_limit.value
    const url_link_val = url_link.value

    if(input_type==resolution){
        if(resolution_val=='Choose your resolution type'){
            resolution.style.borderColor='Red'
        }else{
            resolution.style.borderColor='' 
        }
        // console.log('here')

    } else {
        if(!input_type.value){
          
            input_type.style.borderColor='Red'
           
        }else{
            input_type.style.borderColor=''
        }

        // console.log('here')
    }
}

// Event Handler
downloader_form.addEventListener('submit',e=>{
    e.preventDefault()
    submitRequest()
})
