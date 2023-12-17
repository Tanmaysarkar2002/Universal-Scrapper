import datetime

output_file_location = r'C:\Users\rajva\OneDrive\Desktop\nxt_account_detect\account_detect\output' # file location where we want to store output
file_now = datetime.datetime.now()                   # get the system date time
file_syt_date_time =  file_now.strftime("%y-%m-%d")  # convert the date time to sting format

#=======================================================================================================================================

                                    #>>>>>>>>>>>>>>> IGNORE LIST FUNCTIONS <<<<<<<<<<<<<<#

#========================================================================================================================================

# function to add website in ignore list  
def add_portal_to_IgnoreList(website_name) :
    """
    adds website to ignore list
    
    Parameters
    ----------
    website_name - name of the website
    
    Returns
    -------
    None
    
    """
    file = output_file_location + '\\'  +  'portalignorelist.txt'   
    lo=open(file,"w")      # open the ignore list
    lo.write(website_name) # write website name in ignorelist
    lo.write('\n')         # write newline
    lo.close()             # close the file
    return lo

#===========================================================================================================================================

# function to check website in ignore list
def check_portal_in_IgnoreList(website_name):
    """
    checks if website is present in ignore list
    
    Parameters
    ----------
    website_name - name of the website
    
    Returns
    -------
    None
    
    """
    file = output_file_location + '\\'  +  'portalignorelist.txt' 
    with open(file,"r")as file:      # open the ignore list
        content = file.read()        # read the ignore list
        if website_name in content:  # if website in ignore list return true else false
            return True
        else:
            return False
    
#=====================================================================================================================================
 
                                 #>>>>>>>>>>>>>>> INFO AND ERROR LOG FUNCTIONS <<<<<<<<<<<<<<<<#
 
#=======================================================================================================================================
  
# function to add to info log
def info_log(info_type, website_name,info_stage,info_result,item_value):
    """
    adds info to info log
    
    Parameters
    ----------
    1. info_type - type of info i.e INFO, WARNING ,ERROR, CRITICAL ERROR
    2. website_name - name of the website
    3. info_stage - stage of info i.e process_website1 or process_website2 etc
    4. info_result - starting ,ending
    5. item_value - value of email or mobile number
    
    Returns
    -------
    None
    
    """
    
    file = output_file_location + '\\'  + file_syt_date_time + '-'+ 'info_log.txt' # create seperate file for each website
    fo=open(file, "a")
    now = datetime.datetime.now() # get current system date time
    
    current_syt_date_time =  now.strftime("%y-%m-%d , %H:%M:%S") # convert date time to string 
    fo.write(f"{current_syt_date_time} , {info_type} , {website_name} , {info_stage} , {info_result} , {item_value}")
    fo.write('\n')
    fo.close() # close the file
          
#=============================================================================================================================================  

# function to add error in error log   
def error_log(website_name,item_type,item_value,issue):
    """
    adds error to error log
    
    Parameters
    ----------
    1. website_name - name of the website
    2. item_type - either email type or mobile type
    3. item_value - value of email or mobile number
    4. issue - error issue
    
    Returns
    -------
    None
    
    """
    file = output_file_location + '\\'  + file_syt_date_time + '-'+ 'error.txt' # create seperate error file for each website 
    fo=open(file, "a")
    now = datetime.datetime.now() # get current system date time
    current_syt_date_time =  now.strftime("%y-%m-%d , %H:%M:%S")  # convert date time to string format
    fo.write(f"{current_syt_date_time} , {issue} , {website_name} , {item_type} , {item_value}")
    fo.write('\n')
    fo.close() # close file
    

#=========================================================================================================================================

                            #>>>>>>>>>>>>>>>> FOUND , NOT FOUND , NOT CHECKED LIST FUNCTIONS <<<<<<<<<<<<<<#

#==========================================================================================================================================    

# function to add websites in found list   
def add_to_found_list(website_name,item_type,item_value):
    """
    adds email or mobile number to found list
    
    Parameters
    ----------
    1. website_name - name of the website
    2. item_type - either email or mobile type
    3. item_value - value of email or mobile number
    
    Returns
    -------
    None
    
    """
    file = output_file_location + '\\'  + file_syt_date_time  + '-'+ 'found_list.txt' # create seperate found list for each website
    fo=open(file, "a") # open the file
    now = datetime.datetime.now() # get current system date time
    current_syt_date_time =  now.strftime("%y-%m-%d , %H:%M:%S")  # convert date time to string format
    fo.write(f"{current_syt_date_time} , account found in , {website_name} , with type , {item_type} , and id , {item_value}")
    fo.write('\n')
    fo.close() # close file

#=================================================================================================================================================

# function to add websites in not found list     
def add_to_notfound_list(website_name,item_type,item_value):
    """
    adds email or mobile to not found list
    
    Parameters
    ----------
    1. website_name - name of the website
    2. item_type - either email or mobile type
    3. item_value - value of email or mobile number
    
    Returns
    -------
    None
    
    """
    file = output_file_location + '\\'  + file_syt_date_time  + '-'+ 'notfound_list.txt' # create seperate file for not found list
    fo=open(file, "a") # open the file
    now = datetime.datetime.now()  # get current system date time
    current_syt_date_time =  now.strftime("%y-%m-%d , %H:%M:%S")  # convert date time to string format
    fo.write(f"{current_syt_date_time} , account not found in , {website_name} , with type , {item_type} , and id , {item_value}")
    fo.write('\n')
    fo.close() # close file
     
   
#==========================================================================================================================================
     
# function to add websites to not checked list
def add_to_notchecked_list(website_name,item_value,reason):
    """
    adds website to not checked list
    
    Parameters
    ----------
    1. website_name - name of the website
    2. item_value - value of email or mobiel number
    3. reason - reason why website is being added to notchecked list
    
    Returns
    -------
    None
    
    """
    file = output_file_location + '\\'  + file_syt_date_time + '-'+ 'notchecked_list.txt'
    fo=open(file, "a") # open the file
    now = datetime.datetime.now()  # get current system date time
    current_syt_date_time =  now.strftime("%y-%m-%d , %H:%M:%S")  # convert date time to string format
    fo.write(f"{current_syt_date_time} , website not checked , {website_name} , {item_value} , due to , {reason}")
    fo.write('\n')
    fo.close()  # close file
     


      
#==========================================================================================================================================      
      

    
    
