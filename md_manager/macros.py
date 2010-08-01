info_itens = ['Alerts', 'Comment', 'Immunization', 'Medication', 'Person', 'Problem',
              'Procedure', 'Result', 'SocialHistory']
info_fields = [["Name", 
		        "ApproximateStartDate",
		        "StartDate",
		        "StopDate",
		        "Age",
                "AgeUnit",
                "TreatedBy",
                "Status",
                "Type",
                "Comment",
                "ReactionDescription",
                "ReactionSeverity"], 
               ["CommentDate",
                "Description",
                "Id",
                "SourceId",
                "Type"],
               ["Date",
                "Name",
                "OrderedBy",
                "Route",
                "Site",
                "Type"],
               ["ApproximateDate",
                "BrandName",
                "DirectionDescription",
                "Dose",
                "FilledOn",
                "Frequency",
                "PillStrenghtText",
                "PillStrenghtUnit",
                "PillStrenghtValue",
                "Puantity",
                "RefillsLeft",
                "Route",
                "StartAgeUnit",
                "StartAgeValue",
                "StartDate",
                "Status",
                "StopDate",
                "Type",
                "WrittenBy",
                "WrittenOn"],
               ["Id",
                "GivenName",
                "MiddleName",
                "FamilyName",
                "NickName",
                "DisplayName",
                "Organization",
                "Speciality",
                "AddressLine1",
                "AddressLine2",
                "AddressCity",
                "AddressState",
                "AddressCountry",
                "PostalCode",
                "PhoneNumber",
                "PhoneType",
                "Email",
                "Status",
                "Sex",
                "DateOfBirth",
                "Age",
                "AgeUnit"],
               ["Description",
                "Status",
                "StartDate",
                "StopDate",
                "TreatedBy",
                "Type",
                "Comment"],
               ["Name",
                "StartDate",
                "StopDate",
                "TreatedBy",
                "Type",
                "BeginRangeDate",
                "EndRangeDate",
                "BeginRangeAgeValue",
                "BeginRangeAgeUnit",
                "EndRangeAgeValue",
                "EndRangeAgeUnit",
                "Comment",
                "Status",
                "AgeUnit",
                "AgeValue",
                "ApproximateDate"],
               ["Description",
                "StartDate",
                "TestDescription",
                "TestType",
                "TestFlag",
                "TestStartDate",
                "TestResultUnit",
                "TestResultValue",
                "TestNormal",
                "TestOrderedBy"],
               ["ActorId",
                "Type",
                "Description",
                "Comment",
                "Id"]]
                
informations = [(info_itens[0], info_fields[0]), (info_itens[1], info_fields[1]),
                (info_itens[2], info_fields[2]), (info_itens[3], info_fields[3]),
                (info_itens[4], info_fields[4]), (info_itens[5], info_fields[5]),
                (info_itens[6], info_fields[6]), (info_itens[7], info_fields[7]),
                (info_itens[8], info_fields[8])]

infos_dic = {info_itens[0]: info_fields[0], info_itens[1]: info_fields[1],
             info_itens[2]: info_fields[2], info_itens[3]: info_fields[3],
             info_itens[4]: info_fields[4], info_itens[5]: info_fields[5],
             info_itens[6]: info_fields[6], info_itens[7]: info_fields[7],
             info_itens[8]: info_fields[8]}


