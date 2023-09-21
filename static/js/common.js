var selectedFiles = [];

$(document).ready(function() {

    // $('.parent-loader').fadeOut()

    // Update the value when the user drags the range input
    $('#similarity').on('input', function() {
      const newValue = parseInt(parseFloat($('#similarity').val()) * 100);
      $('#similarityValue').text(newValue+'%');
    });
    $('#stability').on('input', function() {
      const newValue = parseInt(parseFloat($('#stability').val()) * 100);
      $('#stabilityValue').text(newValue+'%');
    });

    $.notify.defaults({
        maxVisible: 1
      });

    currentPath = window.location.pathname.replace(/[^a-zA-Z]+/g, '')

    $('.'+currentPath).addClass('active_nav')
    

    $('#newtable').DataTable({
        searching: true,
        processing: true,
        serverSide: true,
        stateSave: false,
        responsive: true,
        pagination:true, 
        oLanguage: {sProcessing: "<div><div></div><div></div><div></div><div></div></div>"},
        ajax: {
            url: '/pdfitem',
        },
        columns: [
                // { data: 'name' },
                { data: 'status',
                    render: function(data, type, full, meta) {
                        if (data == 'False') {
                            input = '<input type="checkbox" name="" class="checkbox">'
                        }
                        else{
                            input = '<input type="checkbox" name="" class="disabled_checked" disabled>'
                        }
                        return input;
                    } 
                },
                { data: 'id',
                    render: function(data, type, full, meta) {
                        return meta.row + meta.settings._iDisplayStart + 1;
                    }  
                },
                { data: 'upload_on',
                    render: function(data, type, full, meta) {
                        return data.split(' ')[0];
                    }
                },
                { data: 'name', class : "file_name" },
                { data: 'status',
                    render: function(data, type, full, meta) {
                        if (data == 'False') {
                            status = 'Unprocessed'
                        }
                        else{
                            status = 'Done'
                        }
                        return status;
                    }
                },
                { data: 'is_public',
                    render: function(data, type, full, meta) {
                        if (full.is_public == "True"){
                            disable_btn = "disabled"
                        }
                        else{
                            disable_btn = ""
                        }
                        url = window.location.origin
                        return `<div class="flex-box"><a href="media/home/esmee/mouthpiece/pdfs/${full.name}" class="btn-preview btn-orange" target="_blank"> <img src="/static/images/preview.svg" %}"> </a>
                        <a url="${url}/delete_pdf_file/${full.id}" class="btn-preview btn-orange delete_pdf_file" target="_blank"> <img src="/static/images/delete.svg" %}"> </a> 
                        <button  type="button" class="btn-preview btn-preview2 btn-orange move_to_public" ${disable_btn}>Move to Public</button></div>`;
                    }
                },
            ],
    });

    $('#newtable2').DataTable({
        searching: true,
        processing: true,
        serverSide: true,
        stateSave: false,
        responsive: true,
        pagination:true, 
        oLanguage: {sProcessing: "<div><div></div><div></div><div></div><div></div></div>"},  
        ajax: {
            url: '/epubitem',
        },
        columns: [
                // { data: 'name' },
                { data: 'status',
                    render: function(data, type, full, meta) {
                        if (data == 'False') {
                            input = '<input type="checkbox" name="" class="checkbox">'
                        }
                        else{
                            input = '<input type="checkbox" name="" class="disabled_checked" disabled>'
                        }
                        return input;
                    } 
                },
                { data: "id",
                    render: function(data, type, full, meta) {
                        return meta.row + meta.settings._iDisplayStart + 1;
                    }  
                },
                { data: 'upload_on',
                    render: function(data, type, full, meta) {
                        return data.split(' ')[0];
                    }
                },
                { data: 'name', class : "file_name" },
                { data: 'status',
                    render: function(data, type, full, meta) {
                        if (data == 'False') {
                            status = 'Unprocessed'
                        }
                        else{
                            status = 'Done'
                        }
                        return status;
                    }
                },
                { data: 'is_public',
                    render: function(data, type, full, meta) {
                        if (full.is_public == "True"){
                            disable_btn = "disabled"
                        }
                        else{
                            disable_btn = ""
                        }
                        file_name = full.name.replace('.epub', '.pdf')
                        url = window.location.origin
                        return `<div class="flex-box"><a href="media/home/esmee/mouthpiece/ebooks/${file_name}" class="btn-preview btn-orange m-2" target="_blank"> <img src="/static/images/preview.svg" %}"> </a>
                        <a url="${url}/delete_epub_file/${full.id}" class="btn-preview btn-orange delete_epub_file" target="_blank"> <img src="/static/images/delete.svg" %}"> </a> 
                        <button  type="button" class="btn-preview btn-preview2 btn-orange move_to_public" ${disable_btn}>Move to Public</button></div>`;
                    }
                },
            ],
    });

    $('#newtable3').DataTable({
        searching: true,
        processing: true,
        serverSide: true,
        stateSave: false,
        responsive: true,
        pagination:true, 
        oLanguage: {sProcessing: "<div><div></div><div></div><div></div><div></div></div>"},      
        ajax: {
            url: '/htmlitem',
        },
        columns: [
                // { data: 'summary_status',
                //     render: function(data, type, full, meta) {
                //         if (data == 'False') {
                //             input = '<input type="checkbox" name="" class="checkbox">'
                //         }
                //         else{
                //             input = '<input type="checkbox" name="" class="disabled_checked" disabled>'
                //         }
                //         return input;
                //     } 
                // },
                { data: 'id',
                    render: function(data, type, full, meta) {
                        return meta.row + meta.settings._iDisplayStart + 1;
                    }  
                },
                { data: 'upload_on',
                    render: function(data, type, full, meta) {
                        return data.split(' ')[0];
                    }
                },
                { data: 'name',
                  class : "file_name" },
                { data: 'text_to_speech_status',
                    render: function(data, type, full, meta) {
                        if (data == 'False') {
                            status = 'Unprocessed'
                        }
                        else{
                            status = 'Done'
                        }
                        return status;
                    }
                },
                { data: 'is_public',
                    render: function(data, type, full, meta) {
                        if (full.text_to_speech_status == 'False') {
                            status = 'Unprocessed'
                            disable = ''
                            // download = 'download'
                        }
                        else{
                            status = 'Done'
                            disable = 'disabled'
                            // download = 'style="pointer-events: none;"'
                        }
                        if (full.is_public == "True"){
                            disable_btn = "disabled"
                        }
                        else{
                            disable_btn = ""
                        }
                        url = window.location.origin
                        return `<div class="s_${status} flex-box" ${disable}><button type="button" class="btn-preview btn-green" > <a href="media/home/esmee/mouthpiece/htmls/${full.name}" download><img src="static/images/download.svg"></a> </button>
                        <a url="${url}/delete_html_file/${full.id}" class="btn-preview btn-orange delete_html_file" target="_blank"> <img src="/static/images/delete.svg" %}"> </a> 
                        <button type="button" class="btn-preview btn-orange"><a href="media/home/esmee/mouthpiece/htmls/${full.name}" target="_blank"> <img src="/static/images/preview.svg" %}"=""> </a></button>
                        <button type="button" class="btn-preview btn-preview2 btn-orange speechmodal" ${disable} id="${full.name}">Text to speech</button> <button  type="button" class="btn-preview btn-preview2 btn-orange move_to_public" ${disable_btn}>Move to Public</button></div>`
                    }
                },
            ],
    });

    $('#newtable4').DataTable({
        searching: true,
        processing: true,
        serverSide: true,
        stateSave: false,
        responsive: true,
        pagination:true, 
        oLanguage: {sProcessing: "<div><div></div><div></div><div></div><div></div></div>"},
        ajax: {
            url: '/mp3item',
        },
        columns: [                
                { data: 'id',
                    render: function(data, type, full, meta) {
                        return meta.row + meta.settings._iDisplayStart + 1;
                    }  
                },
                { data: 'upload_on',
                    render: function(data, type, full, meta) {
                        return data.split(' ')[0];
                    }
                },
                { data: 'name',
                    render:function(data,type, full, meta){
                        return data.split('/')[1];
                    }},
                { data: 'status',
                    render: function(data, type, full, meta) {
                        url = window.location.origin
                        return `<div class="flex-box"><button type="button" class="btn-preview btn-green"> <a href="media/home/esmee/mouthpiece/mp3s/${full.name}" download ><img src="static/images/download.svg"></a> </button>
                        <a url="${url}/delete_mp3_file/${full.id}" class="btn-preview btn-preview2 btn-orange delete_mp3_file" target="_blank"> <img src="/static/images/delete.svg" %}"> </a> 
                        </div>`
                    }
                },
            ],
    });

    $('#newtable5').DataTable({
        searching: true,
        processing: true,
        serverSide: true,
        stateSave: false,
        responsive: true,
        ordering: true,
        pagination:true, 
        order: [1, 'desc'],
        oLanguage: {sProcessing: "<div><div></div><div></div><div></div><div></div></div>"},
        ajax: {
            url: '/summaryitem',
        },
        columns: [                
                { data: 'id',
                    render: function(data, type, full, meta) {
                        return meta.row + meta.settings._iDisplayStart + 1;
                    }  
                },
                { data: 'upload_on',
                    render: function(data, type, full, meta) {
                        return data.split(' ')[0];
                    }
                },
                { data: 'name' },
                { data: 'name',
                    render: function(data, type, full, meta) {
                        url = window.location.origin
                        return `<div class="flex-box"><button type="button" class="btn-preview btn-green"> <a href="media/home/esmee/mouthpiece/summaries/${full.name}" download><img src="static/images/download.svg"></a> </button>
                        <a url="${url}/delete_summary_file/${full.id}" class="btn-preview btn-preview2 btn-orange delete_summary_file" target="_blank"> <img src="/static/images/delete.svg" %}"> </a> 
                        </div>`
                    }
                },
            ],
    });

    $('#newtable6').DataTable({
        searching: false,
        processing: true,
        serverSide: true,
        stateSave: false,
        responsive: true,
        ordering: false,
        pagination:true, 
        oLanguage: {sProcessing: "<div><div></div><div></div><div></div><div></div></div>"},
        ajax: {
            url: '/publicfileitem',
        },
        columns: [                
                { data: 'id',
                    render: function(data, type, full, meta) {
                        return meta.row + meta.settings._iDisplayStart + 1;
                    }  
                },
                { data: 'name',
                    render: function(data, type, full, meta) {
                        return full[1].upload_on.split(' ')[0].split('T')[0]
                    }
                },
                { data: 'name',
                    render: function(data, type, full, meta) {
                        return full[0].name
                    }
                },
                { data: 'name',
                    render: function(data, type, full, meta) {
                        path = full[0].name.split('.')[1]
                        if (path == "epub" || path == "mobi")
                            path = "ebook"
                        url = window.location.origin
                        return '<div class="flex-box"><div href="media/home/esmee/mouthpiece/'+path+'s/'+full[0].name+'" class="btn-preview btn-preview2 btn-orange copy_text" > Copy Link </div><div class="copied_block d-none">copied</div> <a url="'+url+'/delete_public_file/'+full[2].id+'?name='+full[0].name+'" class="btn-preview btn-orange delete_public_file" target="_blank"> <img src="/static/images/delete.svg" %}"> </a> </div>';
                    }
                },
            ],
    });

    // Chnages made by Surabhi
    $('#textfilestable').DataTable({
        searching: false,
        processing: true,
        serverSide: true,
        stateSave: false,
        responsive: true,
        ordering: false,
        pagination:true, 
        oLanguage: {sProcessing: "<div><div></div><div></div><div></div><div></div></div>"},
        ajax: {
            url: '/textfilesitem',
        },
        columns: [                
                { data: 'id',
                    render: function(data, type, full, meta) {
                        return meta.row + meta.settings._iDisplayStart + 1;
                    }  
                },
                { 
                    data: 'upload_on'
                },
                { 
                    data: 'name'
                },
                { 
                    data: 'total_charachter'
                },
                { 
                    data: 'name',
                    render: function(data, type, full, meta) {
                        url = window.location.origin
                        return `<div class="flex-box"><div href="media/home/esmee/mouthpiece/text/`+data+`" class="split_text btn-preview">
                        <button class="btn-orange btn-preview"><a href="media/home/esmee/mouthpiece/text/${data}" download><img src="static/images/download.svg"></a></button>
                        <a url="${url}/delete_text_file/${full.id}" class="btn-preview btn-orange delete_text_file" target="_blank"> <img src="/static/images/delete.svg" %}"></a>
                        <button class="download_file_modal btn-orange">Split Text</button>
                        </div>`;
                    }
                },
            ],
    });
    // changes end by Surabhi

    $(document).on('click','.wrapper .menubtn',function(){
        $(this).closest('.wrapper').addClass('lesswraper')
        $('aside.sidebar').addClass('fullsidebar')
    })

    $(document).on('click','.delete_pdf_file, .delete_epub_file, .delete_public_file, .delete_summary_file, .delete_mp3_file, .delete_html_file,.delete_text_file',function(){
        url = $(this).attr('url')
        $.ajax({
            type: 'GET',
            url: url,
            success:function(data){
                oneNotificationAtOnce(data.message, data.status);
                $('table:visible').DataTable().draw()
                // $('#newtable2').DataTable().draw()
            },
            error:function(e){
                oneNotificationAtOnce("File not deleted.", 'error');
            }
        });    
    })

    
    $(document).on('click','.closesidebar',function(){
        $(this).closest('.wrapper').removeClass('lesswraper')
        $('aside.sidebar').removeClass('fullsidebar')
    })


    $(document).on('click','.copy_text',function(){
        thisbtn = $(this)
        $('.copied_block').addClass('d-none')
        thisbtn.next().removeClass('d-none')
        setTimeout(function() {
            thisbtn.next().addClass('d-none')
          }, 1000);
        
        var $temp = $("<textarea>"); 
        $("body").append($temp); 
        $temp.val(window.location.origin+'/'+$(this).attr('href')).select(); 
        document.execCommand("copy"); 
        $temp.remove(); 
    });

    $(document).on('click','.checkbox',function(){
        tableId = $(this).closest('table').attr('id')
        if ($('#'+tableId+' .checkbox:checked').length >= 1){
            $('.generate_html, .create_summary').attr('disabled', false)
        }
        else{
            $('.generate_html, .create_summary').attr('disabled', true)
        }
        if ($('#'+tableId+' .checkbox:checked').length >= 5){
            $('#'+tableId+' .checkbox:not(:checked)').attr('disabled', true)
        }
        else {
            $('#'+tableId+' .checkbox:not(:checked)').attr('disabled', false)
        }
    })

    $(document).on('click','.generate_html',function(){
        $(this).attr('disabled', true)
        token = document.getElementsByName("csrfmiddlewaretoken")[0].value
        tableId = $('table:visible').attr('id')
        var frameArray= [];
        $.each($('#'+tableId+' .checkbox:checked'), function(){
            frameArray.push($(this.closest('tr')).find('td:nth-child(4)').text());
        })
        data = new FormData();
        data.append('file_name', frameArray)
        $.ajax({
            method: "post",
            headers: {'X-CSRFToken': token},
            url: '/pdftohtmlandtext',
            data: data,
            processData: false,
            contentType: false,
            dataType: "json",
            beforeSend: function(){
                $('.parent-loader').fadeIn()
            },
            complete: function(){
                $(this).attr('disabled', false)
                $('.parent-loader').fadeOut()
            },
            success:function(data) {
                oneNotificationAtOnce(data.message, data.status);
                $('#newtable').DataTable().draw()
                $('#newtable2').DataTable().draw()
            },
            error: function() {
                oneNotificationAtOnce("There is some issue. Please try again.");
            }
        });
    })

    $(document).on('click','.create_summary',function(){
        $(this).attr('disabled', true)
        token = document.getElementsByName("csrfmiddlewaretoken")[0].value
        tableId = $('table:visible').attr('id')
        var frameArray= [];
        $.each($('#'+tableId+' .checkbox:checked'), function(){
            frameArray.push($(this.closest('tr')).find('td:nth-child(4)').text());
        })
        data = new FormData();
        data.append('file_name', frameArray)
        $.ajax({
            method: "post",
            headers: {'X-CSRFToken': token},
            url: '/create_summmary',
            data: data,
            processData: false,
            contentType: false,
            dataType: "json",
            beforeSend: function(){
                $('.parent-loader').fadeIn()
            },
            complete: function(){
                $(this).attr('disabled', false)
                $('.parent-loader').fadeOut()
                $('#newtable3').DataTable().draw();
            },
            success:function(data) {
                if (data.largefiles){
                    $('.words_note').removeClass('d-none')
                    setTimeout(function() { $('.words_note').addClass('d-none'); }, 7000);
                }
                if (data.message) {
                    oneNotificationAtOnce(data.message, data.status);                    
                }
            },
            error: function() {
                oneNotificationAtOnce("There is some issue. Please try again.");
            }
        });
    })

    
    $(document).on('change','.upload_mutiple_files',function(){ 
        // if (selectedFiles.length > 7){
        //     $('.uploaded_files').addClass('when_data')
        // }
        // else{
        //     $('.uploaded_files').removeClass('when_data')
        // }
        $('.error_msg').addClass('d-none')       
        for(var i = 0 ; i < this.files.length ; i++){
            selectedFiles = selectedFiles.concat(this.files[i]);
            var fileName = this.files[i].name;
            $('.uploaded_files').append(`<div class="files-area hidebox">
            <button type="button" class="btn-close btn-close-custom"></button>
            <h6>${fileName}</h6>
            </div> `);
            }
    })
    
    $(document).on('click','.btn-close-custom',function(){  
        // if (selectedFiles.length > 7){
        //     $('.uploaded_files').addClass('when_data')
        // }
        // else{
        //     $('.uploaded_files').removeClass('when_data')
        // }
        var fileNameToRemove = $(this).siblings('h6').text();  
        selectedFiles = selectedFiles.filter(function(file){
            return file.name !== fileNameToRemove;
        });
        $(this).closest('.files-area').remove();
        $('.upload_mutiple_files').val('')
    })

    $(document).on('click','.upload_files_pdf_epub',function(){ 
        $(this).attr('disabled', true)
        $('.upload_mutiple_files').val('')
        if (selectedFiles.length > 0){            
            token = document.getElementsByName("csrfmiddlewaretoken")[0].value
            formData = new FormData($('#myform').get(0));  
            for(var i = 0 ; i < selectedFiles.length ; i++){
                formData.append('files', selectedFiles[i]);
            }      
            $.ajax({
                method: "post",
                headers: {'X-CSRFToken': token},
                url: '/savepdf',
                data: formData,
                processData: false,
                contentType: false,
                dataType: "json",
                beforeSend: function(){
                    $('.parent-loader').fadeIn()
                },
                complete: function(){
                    $('.upload_files_pdf_epub').attr('disabled', false)
                    $('.parent-loader').fadeOut()
                },
                success:function(data) {
                    selectedFiles = []
                    $('.uploaded_files').empty()
                    $('#uploadmodal').modal('hide')
                    oneNotificationAtOnce(data.message, data.tag);
                    $('#newtable').DataTable().draw()
                    $('#newtable2').DataTable().draw()
                },
                error: function() {
                    oneNotificationAtOnce("There is some issue. Please try again.");
                }
            });
        }
        else{
            // oneNotificationAtOnce("Please select files to upload.");
            $('.error_msg').removeClass('d-none')
        }
    })

    // changes made by Surabhi
    $(document).on('input','#chunk_size', function() {
        var inputValue = $(this).val().trim();
        var submitButton = $('.yes_download');
        if (inputValue === '') {
            submitButton.prop('disabled', true);
        } else {
            submitButton.prop('disabled', false);
        }
    });

    $(document).on('click','.divide_chunks',function(){
    $(this).addClass('d-none');
    $(this).next().addClass('d-none');
    if($('.chunk_size_div').length == 0 ){
        $('.file_url').append(`
        <div class="chunk_size_div d-inline-flex"><input type="number" id="chunk_size" class="form-control radius-custom" required/>
        <button class="btn btn-secondary yes_download" disabled/>Confirm</button>
        </div>
        `)
    }
    })
    


    $(document).on('click','.yes_download',function(){
        file_url = $('.file_url .divide_chunks').attr('id');
        chunks_size = $('#chunk_size').val();
        if(parseInt(chunks_size) <= parseInt($('.file_length').text())){
            divideChunks(file_url,chunks_size)
            $('.chunk_size_div').next('span').remove();
            $('#download_file_modal').modal('hide');
        }
        else{
            if ($('.chunk_size_div').next('span').length > 0 ){
                console.log("")
            } else {
                $('.chunk_size_div').after(`<span class="error_msg d-block" style="color:red; width: 100%; font-size:14px;">Chunk size can not be greater than length of text file</span>`)
            }            
        }
        
    })

    $(document).on('click','.download_file_modal',function(){
        $('.divide_chunks').removeClass('d-none');
        $('.divide_chunks').next().removeClass('d-none');
        $('.chunk_size_div').remove()
        $('.error_msg').addClass('d-none') 
        $('#download_file_modal').modal('show');
        txt_file_path = $(this).parent().attr('href')
        $('.file_url .divide_chunks').attr('id',txt_file_path)
        file_name = $(this).closest('tr').find('td:eq(2)').text()
        getLengthofTextFile(txt_file_path,file_name)
    })

    $(document).on('click','.upload_txt_file',function(){
        $('#uploadmodal').modal('show');
        $('.custom-file>.upload_mutiple_files').attr('accept','.txt');
        $('.uploading-box>.text-center>button').removeClass('upload_files_pdf_epub').addClass('upload_text_files')
        $('.upload_text_files').prop('disabled',false)
    })

    $(document).on('click','.upload_text_files',function(){ 
        $(this).attr('disabled', true)
        $('.upload_mutiple_files').val('')
        if (selectedFiles.length > 0){            
            token = document.getElementsByName("csrfmiddlewaretoken")[0].value
            formData = new FormData($('#myform').get(0));  
            for(var i = 0 ; i < selectedFiles.length ; i++){
                formData.append('files', selectedFiles[i]);
            }      
            $.ajax({
                method: "post",
                headers: {'X-CSRFToken': token},
                url: '/savetext',
                data: formData,
                processData: false,
                contentType: false,
                dataType: "json",
                beforeSend: function(){
                    $('.parent-loader').fadeIn()
                },
                complete: function(){
                    $('.upload_files_pdf_epub').attr('disabled', false)
                    $('.parent-loader').fadeOut()
                },
                success:function(data) {
                    $('.uploaded_files').empty()
                    $('#uploadmodal').modal('hide')
                    oneNotificationAtOnce(data.message, data.tag);
                    $('#textfilestable').DataTable().draw()
                },
                error: function() {
                    oneNotificationAtOnce("There is some issue. Please try again.");
                }
            });
        }
        else{
            $('.error_msg').removeClass('d-none')
        }
    })

   // changes end by Surabhi


    $(document).on('click','#default_value',function(){
        $('#stability').val(0.5);
        $('#stability').next().text('50%')
        $('#similarity').val(0.75);
        $('#similarity').next().text('75%')
    })
    $(document).on('click','.speechmodal',function(){
        $('#audio_file_modal').modal('show')
        $('.audio_file_name').text($(this).attr('id'))
    })
    
    const socket = new WebSocket('ws://3.22.65.185:8086/ws/livec/?token='+$("input[name='csrfmiddlewaretoken']").val());
    
    $(document).on('click','.generate_voice',function(){
        $('#audio_file_modal').modal('hide')
        $('#converting_status').modal('show')
        socket.onmessage = (e) => {
            result = JSON.parse(e.data).status;
            $('.is-visible').text(result);
            if (result == 'Combined all the chunks and file is saved in "Mp3 Files" folder.'){
                $('#converting_status').modal('hide')
            }
        }
        socket.onclose = (e) => {
            console.log("Socket closed!");
        }
        fileName = $('.audio_file_name').text();
        voice_id = $('.voices_opt').val();
        stability = $('#stability').val();
        similarity = $('#similarity').val();
        username = $('.hidden_user').text();
        token = $("input[name='csrfmiddlewaretoken']").val()
        data = {};
        data['file_name']= fileName
        data['voice_id']=voice_id
        data['stability']= stability
        data['similarity']= similarity
        data['username']= username
        socket.send(JSON.stringify(
            {
                type: "authenticate",
                csrfToken: token,
                "data": data
            }
        ))
        // $.ajax({
        //     method: "post",
        //     headers: {'X-CSRFToken': token},
        //     url: '/convert_to_mp3',
        //     data: data,
        //     processData: false,
        //     contentType: false,
        //     dataType: "json",
        //     beforeSend: function(){
        //         $('.parent-loader').fadeIn()
        //     },
        //     complete: function(){
        //         $('.parent-loader').fadeOut()
        //     },
        //     success:function(data) {
        //         if (data.status == 'success'){
        //             oneNotificationAtOnce("MP3 created.", "success");
        //             $('#newtable3').DataTable().draw()
        //         }
        //         else if(data.status){
        //             oneNotificationAtOnce(JSON.parse(data.message).detail.message, "error");
        //         }
        //         else {
        //             oneNotificationAtOnce("MP3 not created.", "error");
        //         }
        //     },
        //     error: function() {
        //         oneNotificationAtOnce("There is some issue. Please try again.");
        //     }
        // });
    });

    $(document).on('click','.move_to_public',function(){
        if ($(this).closest('tr').hasClass('parent')){
            fileName = $(this).closest('tr').find('.file_name').text()
        }
        else  if ($(this).closest('tr').hasClass('child')){
            fileName = $(this).closest('tr').prev('.parent').find('.file_name').text()
        }
        else{
            fileName = $(this).closest('tr').find('.file_name').text()
        }
        token = document.getElementsByName("csrfmiddlewaretoken")[0].value
        data = new FormData();
        data.append('file_name', fileName)
        $.ajax({
            method: "post",
            headers: {'X-CSRFToken': token},
            url: '/move_to_public',
            data: data,
            processData: false,
            contentType: false,
            dataType: "json",
            beforeSend: function(){
                $('.parent-loader').fadeIn()
            },
            complete: function(){
                $('.parent-loader').fadeOut()
            },
            success:function(data) {
                if (data.status == 'success'){
                    oneNotificationAtOnce("File moved to Public folder.", "success");
                    $('#newtable').DataTable().draw()
                    $('#newtable2').DataTable().draw()
                    $('#newtable3').DataTable().draw()
                }
                else {
                    oneNotificationAtOnce("File doesn't moved to Public folder.", "error");
                }
            },
            error: function() {
                oneNotificationAtOnce("There is some issue. Please try again.");
            }
        });
    });

    
})

function oneNotificationAtOnce(message, status='error'){
    $('.notifyjs-corner').empty();
    $.notify(message, status);
}


function handleDragOver(event) {
    event.preventDefault();
    event.dataTransfer.dropEffect = "copy";
  }

function handleDrop(event) {
    event.preventDefault();
    var files = event.dataTransfer.files;
    for(var i = 0 ; i < files.length ; i++){
        console.log(files[i])
        selectedFiles = selectedFiles.concat(files[i]);
        var fileName = files[i].name;
        $('.uploaded_files').append(`<div class="files-area hidebox">
        <button type="button" class="btn-close btn-close-custom"></button>
        <h6>${fileName}</h6>
        </div> `);
        }
  }

// changes made by Surabhi

function getLengthofTextFile(txt_file_path,file_name){
$.ajax({
    method: "GET",
    url: '/get_length_of_txt_file',
    data: {"file_path":txt_file_path},
    beforeSend: function(){
        $('.parent-loader').fadeIn()
    },
    complete: function(){
        $('.parent-loader').fadeOut()
    },
    success:function(data) {
        if (data.status == 'success'){
            $('.file_length').text(data['length'])
            $('.file_name').text(file_name)
        }
        else {
            oneNotificationAtOnce("File doesn't have correct path.", "error");
        }
    },
    error: function() {
        oneNotificationAtOnce("There is some issue. Please try again.");
    }
});
}


function divideChunks(file_url,chunks_size){
$.ajax({
    method: "GET",
    url: '/divide_chunks',
    data: {"file_path":file_url,"chunks_size":chunks_size},
    beforeSend: function(){
        $('.parent-loader').fadeIn()
    },
    complete: function(){
        $('.parent-loader').fadeOut()
    },
    success:function(data) {
        if (data.status == 'success'){
            oneNotificationAtOnce("Chunks created.", "success");
            $('#textfilestable').DataTable().draw()
            oneNotificationAtOnce("Files created", "success");
        }
        else {
            oneNotificationAtOnce("There is some issue. Please try again.", "error");
        }
    },
    error: function() {
        oneNotificationAtOnce("There is some issue. Please try again.");
    }
});
}
//end changes made by Surabhi