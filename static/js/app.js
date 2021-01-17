
const resolution = document.querySelector('.resolution')
const lower_limit = document.querySelector('.lower_limit')
const upper_limit = document.querySelector('.upper_limit')
const url_link = document.querySelector('.url_link')
const submit_btn = document.querySelector('.submit_btn')
const downloader_form = document.querySelector('.downloader_form')
const playlist_option=document.querySelector('#flexRadioDefault1')
const single_vid_option=document.querySelector('#flexRadioDefault2')
const spinner_box=document.querySelector('.spinner_box')
const download_box=document.querySelector('.download_box')
const download_link=document.querySelector('.download_link')


// fetch action
async function postAPI(data){

    const response= await fetch('/video-download',{
        method: 'POST', 
        // mode: 'cors', 
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
    let lower_limit_val = lower_limit.value
    let upper_limit_val 
    // let upper_limit_val = upper_limit.value
    const url_link_val = url_link.value

    

    if(playlist_option.checked){
        validateInput(resolution)
        validateInput(upper_limit)
        validateInput(lower_limit)
        validateInput(url_link)

        upper_limit_val=validateRange(resolution_val,lower_limit_val,upper_limit.value)
        submit_btn.disabled=true

        if (resolution_val && lower_limit_val && upper_limit_val && url_link_val){
            spinner_box.classList.remove('d-none')
            
            postAPI({
                'ul':upper_limit_val,
                'll':parseInt(lower_limit_val),
                'url':url_link_val,
                'playlist': true,
                'resolution':resolution_val
            }).then(data=>{
                console.log(data)
                spinner_box.classList.add('d-none')
                download_box.classList.remove('d-none')
                download_link.setAttribute('href',data.media_link)
                submit_btn.disabled=false
            }).catch(e=>{
                console.log(e)
                submit_btn.disabled=false
                spinner_box.innerHTML='<h4>Sorry, an error happened while downloading your video. Please try again. Thank you</h4>'
            })
        }
    }else{
        
        validateInput(resolution)
        validateInput(url_link)
        if (resolution_val && url_link_val){
            postAPI({
                'url':url_link_val,
                'playlist': false,
                'resolution':resolution_val
            }).then(data=>{
                console.log(data)
                spinner_box.classList.add('d-none')
                download_box.classList.remove('d-none')
                download_link.setAttribute('href',data.media_link)
            }).catch(e=>{
                console.log(e)
                spinner_box.innerHTML='<h4>Sorry, an error happened while downloading your video. Please try again. Thank you</h4>'

            })
        }
    }

}


function validateInput(input_type){


    if(input_type==resolution){
        if(input_type.value==''){
            resolution.style.borderColor='Red'
        }else{
            resolution.style.borderColor='' 
        }

    } else {
        if(!input_type.value){
          
            input_type.style.borderColor='Red'
           
        }else{
            input_type.style.borderColor=''
        }

    }
}

function disableFields(){
    if(single_vid_option.checked){
        lower_limit.disabled=true
        upper_limit.disabled=true
    }else{
        lower_limit.disabled=false
        upper_limit.disabled=false
    }
}

function validateRange(resolution_val,lower_limit_val,upper_limit_val){

    const diff= parseInt(upper_limit_val)-parseInt(lower_limit_val)
   

    if(resolution_val==='360p' && diff>20){
        upper_limit_val=parseInt(lower_limit_val)+19
        upper_limit.value=upper_limit_val
        return upper_limit_val
    }else if(resolution_val==='480p' && diff>15){
        upper_limit_val=parseInt(lower_limit_val)+14
        upper_limit.value=upper_limit_val
        return upper_limit_val
    }else if (resolution_val==='720p' && diff>10){
        upper_limit_val=parseInt(lower_limit_val)+9
        upper_limit.value=upper_limit_val
        return upper_limit_val

    }else if (resolution_val==='1080p' && diff>5){
        upper_limit_val=parseInt(lower_limit_val)+4
        upper_limit.value=upper_limit_val
        return upper_limit_val

    }else{
     upper_limit_val = upper_limit.value
     return upper_limit_val
    }

}

// Event Handler
downloader_form.addEventListener('submit',e=>{
    e.preventDefault()
    submitRequest()
})

single_vid_option.addEventListener('click',disableFields)
playlist_option.addEventListener('click',disableFields)