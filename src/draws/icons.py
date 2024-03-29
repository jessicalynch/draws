"""Maps AWS resource types to SVG icons."""

# TODO: refactor to support aliases
icon_mapping = {
    "AWS-Lambda-Function": "Res_AWS-Lambda_Lambda-Function_48.svg",
    "AWS-ApiGateway": "Arch_Amazon-API-Gateway_64.svg",
    "AWS-ApiGatewayV2": "Arch_Amazon-API-Gateway_64.svg",
    "AWS-EC2": "Arch_Amazon-EC2_64.svg",
    "AWS-Kinesis": "Arch_Amazon-Kinesis_64.svg",
    "AWS-KinesisFirehose": "Arch_Amazon-Kinesis-Data-Firehose_64.svg",
    "AWS-S3-Bucket": "Res_Amazon-Simple-Storage-Service_Bucket_48.svg",
    "AWS-S3": "Arch_Amazon-Simple-Storage-Service_64.svg",
    "Custom-S3BucketNotifications": "Arch_Amazon-Simple-Storage-Service_64.svg",
    "Custom-S3AutoDeleteObjects": "Arch_Amazon-Simple-Storage-Service_64.svg",
    "AWS-Cloud-Development-Kit": "Arch_AWS-Cloud-Development-Kit_64.svg",
    "AWS-IAM": "Arch_AWS-Identity-and-Access-Management_64.svg",
    "AWS-IAM-Role": "Res_AWS-Identity-Access-Management_Role_48.svg",
    "AWS-DynamoDB": "Arch_Amazon-DynamoDB_64.svg",
    "AWS-Lambda": "Arch_AWS-Lambda_64.svg",
    "AWS-Cognito": "Arch_Amazon-Cognito_64.svg",
    "AWS-AppStream": "Arch_Amazon-AppStream_64.svg",
    "AWS-WorkSpaces-Family": "Arch_Amazon-WorkSpaces-Family_64.svg",
    "AWS-WorkLink": "Arch_Amazon-WorkLink_64.svg",
    "AWS-Elastic-Beanstalk": "Arch_AWS-Elastic-Beanstalk_64.svg",
    "AWS-Serverless-Application-Repository": "Arch_AWS-Serverless-Application-Repository_64.svg",
    "Elastic-Fabric-Adapter": "Arch_Elastic-Fabric-Adapter_64.svg",
    "AWS-Wavelength": "Arch_AWS-Wavelength_64.svg",
    "AWS-Outposts-servers": "Arch_AWS-Outposts-servers_64.svg",
    "NICE-EnginFrame": "Arch_NICE-EnginFrame_64.svg",
    "AWS-Thinkbox-Deadline": "Arch_AWS-Thinkbox-Deadline_64.svg",
    "AWS-SimSpace-Weaver": "Arch_AWS-SimSpace-Weaver_64.svg",
    "AWS-Thinkbox-Stoke": "Arch_AWS-Thinkbox-Stoke_64.svg",
    "NICE-DCV": "Arch_NICE-DCV_64.svg",
    "AWS-Nitro-Enclaves": "Arch_AWS-Nitro-Enclaves_64.svg",
    "AWS-Parallel-Cluster": "Arch_AWS-Parallel-Cluster_64.svg",
    "AWS-Compute-Optimizer": "Arch_AWS-Compute-Optimizer_64.svg",
    "Bottlerocket": "Arch_Bottlerocket_64.svg",
    "AWS-Thinkbox-Sequoia": "Arch_AWS-Thinkbox-Sequoia_64.svg",
    "AWS-Outposts-rack": "Arch_AWS-Outposts-rack_64.svg",
    "AWS-Thinkbox-XMesh": "Arch_AWS-Thinkbox-XMesh_64.svg",
    "AWS-Outposts-family": "Arch_AWS-Outposts-family_64.svg",
    "AWS-Genomics-CLI": "Arch_Amazon-Genomics-CLI_64.svg",
    "AWS-Thinkbox-Frost": "Arch_AWS-Thinkbox-Frost_64.svg",
    "AWS-Lightsail-for-Research": "Arch_Amazon-Lightsail-for-Research_64.svg",
    "AWS-Batch": "Arch_AWS-Batch_64.svg",
    "AWS-EC2-Auto-Scaling": "Arch_Amazon-EC2-Auto-Scaling_64.svg",
    "AWS-App-Runner": "Arch_AWS-App-Runner_64.svg",
    "AWS-Lightsail": "Arch_Amazon-Lightsail_64.svg",
    "AWS-Thinkbox-Krakatoa": "Arch_AWS-Thinkbox-Krakatoa_64.svg",
    "AWS-EC2-Image-Builder": "Arch_Amazon-EC2-Image-Builder_64.svg",
    "AWS-Local-Zones": "Arch_AWS-Local-Zones_64.svg",
    "VMware-Cloud-on-AWS": "Arch_VMware-Cloud-on-AWS_64.svg",
    "AWS-Neptune": "Arch_Amazon-Neptune_64.svg",
    "AWS-Timestream": "Arch_Amazon-Timestream_64.svg",
    "AWS-RDS": "Arch_Amazon-RDS_64.svg",
    "AWS-ElastiCache": "Arch_Amazon-ElastiCache_64.svg",
    "AWS-Aurora": "Arch_Amazon-Aurora_64.svg",
    "AWS-Keyspaces": "Arch_Amazon-Keyspaces_64.svg",
    "AWS-RDS-on-VMware": "Arch_Amazon-RDS-on-VMware_64.svg",
    "AWS-Database-Migration-Service": "Arch_AWS-Database-Migration-Service_64.svg",
    "AWS-MemoryDB-for-Redis": "Arch_Amazon-MemoryDB-for-Redis_64.svg",
    "AWS-DocumentDB": "Arch_Amazon-DocumentDB_64.svg",
    "AWS-Managed-Services": "Arch_AWS-Managed-Services_64.svg",
    "AWS-IQ": "Arch_AWS-IQ_64.svg",
    "AWS-Professional-Services": "Arch_AWS-Professional-Services_64.svg",
    "AWS-rePost": "Arch_AWS-rePost_64.svg",
    "AWS-Training-Certification": "Arch_AWS-Training-Certification_64.svg",
    "AWS-Activate": "Arch_AWS-Activate_64.svg",
    "AWS-Support": "Arch_AWS-Support_64.svg",
    "AWS-Application-Cost-Profiler": "Arch_AWS-Application-Cost-Profiler_64.svg",
    "Reserved-Instance-Reporting": "Arch_Reserved-Instance-Reporting_64.svg",
    "AWS-Cost-Explorer": "Arch_AWS-Cost-Explorer_64.svg",
    "Savings-Plans": "Arch_Savings-Plans_64.svg",
    "AWS-Cost-and-Usage-Report": "Arch_AWS-Cost-and-Usage-Report_64.svg",
    "AWS-Budgets": "Arch_AWS-Budgets_64.svg",
    "AWS-Billing-Conductor": "Arch_AWS-Billing-Conductor_64.svg",
    "AWS-Signer": "Arch_AWS-Signer_64.svg",
    "AWS-WAF": "Arch_AWS-WAF_64.svg",
    "AWS-GuardDuty": "Arch_Amazon-GuardDuty_64.svg",
    "AWS-CloudHSM": "Arch_AWS-CloudHSM_64.svg",
    "AWS-Audit-Manager": "Arch_AWS-Audit-Manager_64.svg",
    "AWS-Detective": "Arch_Amazon-Detective_64.svg",
    "AWS-Shield": "Arch_AWS-Shield_64.svg",
    "AWS-Macie": "Arch_Amazon-Macie_64.svg",
    "AWS-Firewall-Manager": "Arch_AWS-Firewall-Manager_64.svg",
    "AWS-Network-Firewall": "Arch_AWS-Network-Firewall_64.svg",
    "AWS-Inspector": "Arch_Amazon-Inspector_64.svg",
    "AWS-Artifact": "Arch_AWS-Artifact_64.svg",
    "AWS-Cloud-Directory": "Arch_Amazon-Cloud-Directory_64.svg",
    "AWS-Cognito": "Arch_Amazon-Cognito_64.svg",
    "AWS-Resource-Access-Manager": "Arch_AWS-Resource-Access-Manager_64.svg",
    "AWS-Security-Hub": "Arch_AWS-Security-Hub_64.svg",
    "AWS-Security-Lake": "Arch_Amazon-Security-Lake_64.svg",
    "AWS-Key-Management-Service": "Arch_AWS-Key-Management-Service_64.svg",
    "AWS-Private-Certificate-Authority": "Arch_AWS-Private-Certificate-Authority_64.svg",
    "AWS-Certificate-Manager": "Arch_AWS-Certificate-Manager_64.svg",
    "AWS-Verified-Permissions": "Arch_Amazon-Verified-Permissions_64.svg",
    "AWS-IAM-Identity-Center": "Arch_AWS-IAM-Identity-Center_64.svg",
    "AWS-Payment-Cryptography": "Arch_AWS-Payment-Cryptography_64.svg",
    "AWS-Secrets-Manager": "Arch_AWS-Secrets-Manager_64.svg",
    "AWS-Directory-Service": "Arch_AWS-Directory-Service_64.svg",
    "AWS-Pinpoint-APIs": "Arch_Amazon-Pinpoint-APIs_64.svg",
    "AWS-Wickr": "Arch_AWS-Wickr_64.svg",
    "AWS-AppFabric": "Arch_AWS-AppFabric_64.svg",
    "AWS-Pinpoint": "Arch_Amazon-Pinpoint_64.svg",
    "AWS-WorkDocs": "Arch_Amazon-WorkDocs_64.svg",
    "AWS-Chime-SDK": "Arch_Amazon-Chime-SDK_64.svg",
    "AWS-Supply-Chain": "Arch_AWS-Supply-Chain_64.svg",
    "AWS-Connect": "Arch_Amazon-Connect_64.svg",
    "AWS-Honeycode": "Arch_Amazon-Honeycode_64.svg",
    "AWS-Simple-Email-Service": "Arch_Amazon-Simple-Email-Service_64.svg",
    "AWS-WorkMail": "Arch_Amazon-WorkMail_64.svg",
    "AWS-Chime": "Arch_Amazon-Chime_64.svg",
    "Alexa-For-Business": "Arch_Alexa-For-Business_64.svg",
    "AWS-WorkDocs-SDK": "Arch_Amazon-WorkDocs-SDK_64.svg",
    "AWS-Quantum-Ledger-Database": "Arch_Amazon-Quantum-Ledger-Database_64.svg",
    "AWS-Managed-Blockchain": "Arch_Amazon-Managed-Blockchain_64.svg",
    "AWS-Braket": "Arch_Amazon-Braket_64.svg",
    "AWS-Events-Rule": "Res_Amazon-EventBridge_Rule_48.svg",
    "AWS-IoT-Events": "Arch_AWS-IoT-Events_64.svg",
    "AWS-IoT-Device-Defender": "Arch_AWS-IoT-Device-Defender_64.svg",
    "AWS-IoT-RoboRunner": "Arch_AWS-IoT-RoboRunner_64.svg",
    "AWS-IoT-TwinMaker": "Arch_AWS-IoT-TwinMaker_64.svg",
    "AWS-IoT-Button": "Arch_AWS-IoT-Button_64.svg",
    "FreeRTOS": "Arch_FreeRTOS_64.svg",
    "AWS-IoT-SiteWise": "Arch_AWS-IoT-SiteWise_64.svg",
    "AWS-IoT-Things-Graph": "Arch_AWS-IoT-Things-Graph_64.svg",
    "AWS-IoT-Core": "Arch_AWS-IoT-Core_64.svg",
    "AWS-IoT-ExpressLink": "Arch_AWS-IoT-ExpressLink_64.svg",
    "AWS-IoT-1-Click": "Arch_AWS-IoT-1-Click_64.svg",
    "AWS-IoT-Device-Management": "Arch_AWS-IoT-Device-Management_64.svg",
    "AWS-IoT-Analytics": "Arch_AWS-IoT-Analytics_64.svg",
    "AWS-IoT-FleetWise": "Arch_AWS-IoT-FleetWise_64.svg",
    "AWS-IoT-Greengrass": "Arch_AWS-IoT-Greengrass_64.svg",
    "AWS-RoboMaker": "Arch_AWS-RoboMaker_64.svg",
    "AWS-Application-Composer": "Arch_AWS-Application-Composer_64.svg",
    "AWS-Corretto": "Arch_Amazon-Corretto_64.svg",
    "AWS-X-Ray": "Arch_AWS-X-Ray_64.svg",
    "AWS-CodeCatalyst": "Arch_Amazon-CodeCatalyst_64.svg",
    "AWS-CodeArtifact": "Arch_AWS-CodeArtifact_64.svg",
    "AWS-CodePipeline": "Arch_AWS-CodePipeline_64.svg",
    "AWS-Command-Line-Interface": "Arch_AWS-Command-Line-Interface_64.svg",
    "AWS-Tools-and-SDKs": "Arch_AWS-Tools-and-SDKs_64.svg",
    "AWS-CodeStar": "Arch_AWS-CodeStar_64.svg",
    "AWS-CloudShell": "Arch_AWS-CloudShell_64.svg",
    "AWS-CodeDeploy": "Arch_AWS-CodeDeploy_64.svg",
    "AWS-CodeBuild": "Arch_AWS-CodeBuild_64.svg",
    "AWS-Cloud9": "Arch_AWS-Cloud9_64.svg",
    "AWS-CodeCommit": "Arch_AWS-CodeCommit_64.svg",
    "AWS-Cloud-Control-API": "Arch_AWS-Cloud-Control-API_64.svg",
    "AWS-Marketplace_Dark": "Arch_AWS-Marketplace_Dark_64.svg",
    "AWS-Marketplace_Light": "Arch_AWS-Marketplace_Light_64.svg",
    "Red-Hat-OpenShift-Service-on-AWS": "Arch_Red-Hat-OpenShift-Service-on-AWS_64.svg",
    "AWS-Elastic-Container-Registry": "Arch_Amazon-Elastic-Container-Registry_64.svg",
    "AWS-Elastic-Kubernetes-Service": "Arch_Amazon-Elastic-Kubernetes-Service_64.svg",
    "AWS-Fargate": "Arch_AWS-Fargate_64.svg",
    "AWS-EKS-Distro": "Arch_Amazon-EKS-Distro_64.svg",
    "AWS-ECS-Anywhere": "Arch_Amazon-ECS-Anywhere_64.svg",
    "AWS-Elastic-Container-Service": "Arch_Amazon-Elastic-Container-Service_64.svg",
    "AWS-EKS-Anywhere": "Arch_Amazon-EKS-Anywhere_64.svg",
    "AWS-EKS-Cloud": "Arch_Amazon-EKS-Cloud_64.svg",
    "AWS-Backint-Agent": "Arch_AWS-Backint-Agent_64.svg",
    "AWS-Distro-for-OpenTelemetry": "Arch_AWS-Distro-for-OpenTelemetry_64.svg",
    "AWS-Resilience-Hub": "Arch_AWS-Resilience-Hub_64.svg",
    "AWS-Fault-Injection-Simulator": "Arch_AWS-Fault-Injection-Simulator_64.svg",
    "AWS-Chatbot": "Arch_AWS-Chatbot_64.svg",
    "AWS-OpsWorks": "Arch_AWS-OpsWorks_64.svg",
    "AWS-Control-Tower": "Arch_AWS-Control-Tower_64.svg",
    "AWS-Health-Dashboard": "Arch_AWS-Health-Dashboard_64.svg",
    "AWS-Application-Auto-Scaling": "Arch_AWS-Application-Auto-Scaling_64.svg",
    "AWS-Auto-Scaling": "Arch_AWS-Auto-Scaling_64.svg",
    "AWS-Resource-Explorer": "Arch_AWS-Resource-Explorer_64.svg",
    "AWS-Well-Architected-Tool": "Arch_AWS-Well-Architected-Tool_64.svg",
    "AWS-CloudTrail": "Arch_AWS-CloudTrail_64.svg",
    "AWS-Proton": "Arch_AWS-Proton_64.svg",
    "AWS-CloudFormation": "Arch_AWS-CloudFormation_64.svg",
    "AWS-Managed-Grafana": "Arch_Amazon-Managed-Grafana_64.svg",
    "AWS-Launch-Wizard": "Arch_AWS-Launch-Wizard_64.svg",
    "AWS-Management-Console": "Arch_AWS-Management-Console_64.svg",
    "AWS-Organizations": "Arch_AWS-Organizations_64.svg",
    "AWS-License-Manager": "Arch_AWS-License-Manager_64.svg",
    "AWS-Service-Management-Connector": "Arch_AWS-Service-Management-Connector_64.svg",
    "AWS-Systems-Manager": "Arch_AWS-Systems-Manager_64.svg",
    "AWS-Telco-Network-Builder": "Arch_AWS-Telco-Network-Builder_64.svg",
    "AWS-Trusted-Advisor": "Arch_AWS-Trusted-Advisor_64.svg",
    "AWS-CloudWatch": "Arch_Amazon-CloudWatch_64.svg",
    "AWS-Config": "Arch_AWS-Config_64.svg",
    "AWS-Managed-Service-for-Prometheus": "Arch_Amazon-Managed-Service-for-Prometheus_64.svg",
    "AWS-AppConfig": "Arch_AWS-AppConfig_64.svg",
    "AWS-Service-Catalog": "Arch_AWS-Service-Catalog_64.svg",
    "AWS-EventBridge": "Arch_Amazon-EventBridge_64.svg",
    "AWS-Managed-Workflows-for-Apache-Airflow": "Arch_Amazon-Managed-Workflows-for-Apache-Airflow_64.svg",
    "AWS-AppSync": "Arch_AWS-AppSync_64.svg",
    "AWS-Simple-Notification-Service": "Arch_Amazon-Simple-Notification-Service_64.svg",
    "AWS-Console-Mobile-Application": "Arch_AWS-Console-Mobile-Application_64.svg",
    "AWS-Simple-Queue-Service": "Arch_Amazon-Simple-Queue-Service_64.svg",
    "AWS-AppFlow": "Arch_Amazon-AppFlow_64.svg",
    "AWS-Express-Workflows": "Arch_AWS-Express-Workflows_64.svg",
    "AWS-Step-Functions": "Arch_AWS-Step-Functions_64.svg",
    "AWS-MQ": "Arch_Amazon-MQ_64.svg",
    "AWS-GameLift": "Arch_Amazon-GameLift_64.svg",
    "AWS-GameSparks": "Arch_Amazon-GameSparks_64.svg",
    "Open-3D-Engine": "Arch_Open-3D-Engine_64.svg",
    "AWS-GameKit": "Arch_AWS-GameKit_64.svg",
    "AWS-Elemental-MediaStore": "Arch_AWS-Elemental-MediaStore_64.svg",
    "AWS-Nimble-Studio": "Arch_Amazon-Nimble-Studio_64.svg",
    "AWS-Elemental-Server": "Arch_AWS-Elemental-Server_64.svg",
    "AWS-Elemental-MediaLive": "Arch_AWS-Elemental-MediaLive_64.svg",
    "AWS-Elemental-Appliances-&-Software": "Arch_AWS-Elemental-Appliances-&-Software_64.svg",
    "AWS-Elemental-Link": "Arch_AWS-Elemental-Link_64.svg",
    "AWS-Elemental-MediaConnect": "Arch_AWS-Elemental-MediaConnect_64.svg",
    "AWS-Interactive-Video-Service": "Arch_Amazon-Interactive-Video-Service_64.svg",
    "AWS-Elemental-Live": "Arch_AWS-Elemental-Live_64.svg",
    "AWS-Elemental-Conductor": "Arch_AWS-Elemental-Conductor_64.svg",
    "AWS-Elemental-Delta": "Arch_AWS-Elemental-Delta_64.svg",
    "AWS-Elemental-MediaConvert": "Arch_AWS-Elemental-MediaConvert_64.svg",
    "AWS-Elastic-Transcoder": "Arch_Amazon-Elastic-Transcoder_64.svg",
    "AWS-Elemental-MediaPackage": "Arch_AWS-Elemental-MediaPackage_64.svg",
    "AWS-Kinesis-Video-Streams": "Arch_Amazon-Kinesis-Video-Streams_64.svg",
    "AWS-Elemental-MediaTailor": "Arch_AWS-Elemental-MediaTailor_64.svg",
    "AWS-DeepLens": "Arch_AWS-DeepLens_64.svg",
    "AWS-Bedrock": "Arch_Amazon-Bedrock_64.svg",
    "TorchServe": "Arch_TorchServe_64.svg",
    "AWS-DeepRacer": "Arch_AWS-DeepRacer_64.svg",
    "Apache-MXNet-on-AWS": "Arch_Apache-MXNet-on-AWS_64.svg",
    "AWS-Polly": "Arch_Amazon-Polly_64.svg",
    "AWS-HealthLake": "Arch_AWS-HealthLake_64.svg",
    "AWS-HealthScribe": "Arch_AWS-HealthScribe_64.svg",
    "AWS-HealthOmics": "Arch_AWS-HealthOmics_64.svg",
    "AWS-Rekognition": "Arch_Amazon-Rekognition_64.svg",
    "AWS-Forecast": "Arch_Amazon-Forecast_64.svg",
    "AWS-Augmented-AI-A2I": "Arch_Amazon-Augmented-AI-A2I_64.svg",
    "AWS-Lookout-for-Equipment": "Arch_Amazon-Lookout-for-Equipment_64.svg",
    "AWS-SageMaker-Studio-Lab": "Arch_Amazon-SageMaker-Studio-Lab_64.svg",
    "AWS-Personalize": "Arch_Amazon-Personalize_64.svg",
    "AWS-Textract": "Arch_Amazon-Textract_64.svg",
    "AWS-Elastic-Inference": "Arch_Amazon-Elastic-Inference_64.svg",
    "AWS-Lookout-for-Metrics": "Arch_Amazon-Lookout-for-Metrics_64.svg",
    "AWS-Comprehend-Medical": "Arch_Amazon-Comprehend-Medical_64.svg",
    "AWS-CodeGuru": "Arch_Amazon-CodeGuru_64.svg",
    "AWS-Comprehend": "Arch_Amazon-Comprehend_64.svg",
    "AWS-Kendra": "Arch_Amazon-Kendra_64.svg",
    "TensorFlow-on-AWS": "Arch_TensorFlow-on-AWS_64.svg",
    "AWS-SageMaker-Ground-Truth": "Arch_Amazon-SageMaker-Ground-Truth_64.svg",
    "AWS-Lex": "Arch_Amazon-Lex_64.svg",
    "AWS-Panorama": "Arch_AWS-Panorama_64.svg",
    "AWS-HealthImaging": "Arch_AWS-HealthImaging_64.svg",
    "AWS-Fraud-Detector": "Arch_Amazon-Fraud-Detector_64.svg",
    "AWS-Neuron": "Arch_AWS-Neuron_64.svg",
    "AWS-CodeWhisperer": "Arch_Amazon-CodeWhisperer_64.svg",
    "AWS-Translate": "Arch_Amazon-Translate_64.svg",
    "AWS-Deep-Learning-Containers": "Arch_AWS-Deep-Learning-Containers_64.svg",
    "AWS-Lookout-for-Vision": "Arch_Amazon-Lookout-for-Vision_64.svg",
    "AWS-DevOps-Guru": "Arch_Amazon-DevOps-Guru_64.svg",
    "AWS-Deep-Learning-AMIs": "Arch_AWS-Deep-Learning-AMIs_64.svg",
    "AWS-DeepComposer": "Arch_AWS-DeepComposer_64.svg",
    "AWS-Transcribe": "Arch_Amazon-Transcribe_64.svg",
    "AWS-Monitron": "Arch_Amazon-Monitron_64.svg",
    "AWS-SageMaker": "Arch_Amazon-SageMaker_64.svg",
    "AWS-Application-Migration-Service": "Arch_AWS-Application-Migration-Service_64.svg",
    "AWS-Application-Discovery-Service": "Arch_AWS-Application-Discovery-Service_64.svg",
    "AWS-Migration-Evaluator": "Arch_AWS-Migration-Evaluator_64.svg",
    "AWS-Migration-Hub": "Arch_AWS-Migration-Hub_64.svg",
    "AWS-Mainframe-Modernization": "Arch_AWS-Mainframe-Modernization_64.svg",
    "AWS-DataSync": "Arch_AWS-DataSync_64.svg",
    "AWS-Transfer-Family": "Arch_AWS-Transfer-Family_64.svg",
    "AWS-Ground-Station": "Arch_AWS-Ground-Station_64.svg",
    "AWS-FSx-for-WFS": "Arch_Amazon-FSx-for-WFS_64.svg",
    "AWS-File-Cache": "Arch_Amazon-File-Cache_64.svg",
    "AWS-Snowball-Edge": "Arch_AWS-Snowball-Edge_64.svg",
    "AWS-FSx-for-OpenZFS": "Arch_Amazon-FSx-for-OpenZFS_64.svg",
    "AWS-Snowball": "Arch_AWS-Snowball_64.svg",
    "AWS-Snowcone": "Arch_AWS-Snowcone_64.svg",
    "AWS-Storage-Gateway": "Arch_AWS-Storage-Gateway_64.svg",
    "AWS-Simple-Storage-Service-Glacier": "Arch_Amazon-Simple-Storage-Service-Glacier_64.svg",
    "AWS-Snowmobile": "Arch_AWS-Snowmobile_64.svg",
    "AWS-Backup": "Arch_AWS-Backup_64.svg",
    "AWS-S3-on-Outposts": "Arch_Amazon-S3-on-Outposts_64.svg",
    "AWS-EFS": "Arch_Amazon-EFS_64.svg",
    "AWS-Elastic-Disaster-Recovery": "Arch_AWS-Elastic-Disaster-Recovery_64.svg",
    "AWS-Elastic-Block-Store": "Arch_Amazon-Elastic-Block-Store_64.svg",
    "AWS-FSx-for-NetApp-ONTAP": "Arch_Amazon-FSx-for-NetApp-ONTAP_64.svg",
    "AWS-FSx": "Arch_Amazon-FSx_64.svg",
    "AWS-FSx-for-Lustre": "Arch_Amazon-FSx-for-Lustre_64.svg",
    "AWS-Amplify": "Arch_AWS-Amplify_64.svg",
    "AWS-Device-Farm": "Arch_AWS-Device-Farm_64.svg",
    "AWS-Location-Service": "Arch_Amazon-Location-Service_64.svg",
    "AWS-Entity-Resolution": "Arch_AWS-Entity-Resolution_64.svg",
    "AWS-Managed-Service-for-Apache-Flink": "Arch_Amazon-Managed-Service-for-Apache-Flink_64.svg",
    "AWS-FinSpace": "Arch_Amazon-FinSpace_64.svg",
    "AWS-Glue-DataBrew": "Arch_AWS-Glue-DataBrew_64.svg",
    "AWS-CloudSearch": "Arch_Amazon-CloudSearch_64.svg",
    "AWS-Glue-Elastic-Views": "Arch_AWS-Glue-Elastic-Views_64.svg",
    "AWS-OpenSearch-Service": "Arch_Amazon-OpenSearch-Service_64.svg",
    "AWS-Redshift": "Arch_Amazon-Redshift_64.svg",
    "AWS-QuickSight": "Arch_Amazon-QuickSight_64.svg",
    "AWS-Data-Pipeline": "Arch_AWS-Data-Pipeline_64.svg",
    "AWS-EMR": "Arch_Amazon-EMR_64.svg",
    "AWS-Glue": "Arch_AWS-Glue_64.svg",
    "AWS-Athena": "Arch_Amazon-Athena_64.svg",
    "AWS-Lake-Formation": "Arch_AWS-Lake-Formation_64.svg",
    "AWS-Data-Exchange": "Arch_AWS-Data-Exchange_64.svg",
    "AWS-Kinesis-Data-Streams": "Arch_Amazon-Kinesis-Data-Streams_64.svg",
    "AWS-DataZone": "Arch_Amazon-DataZone_64.svg",
    "AWS-Clean-Rooms": "Arch_AWS-Clean-Rooms_64.svg",
    "AWS-Managed-Streaming-for-Apache-Kafka": "Arch_Amazon-Managed-Streaming-for-Apache-Kafka_64.svg",
    "AWS-PrivateLink": "Arch_AWS-PrivateLink_64.svg",
    "AWS-VPC-Lattice": "Arch_Amazon-VPC-Lattice_64.svg",
    "AWS-Cloud-WAN": "Arch_AWS-Cloud-WAN_64.svg",
    "AWS-Site-to-Site-VPN": "Arch_AWS-Site-to-Site-VPN_64.svg",
    "AWS-Private-5G": "Arch_AWS-Private-5G_64.svg",
    "Elastic-Load-Balancing": "Arch_Elastic-Load-Balancing_64.svg",
    "AWS-Virtual-Private-Cloud": "Arch_Amazon-Virtual-Private-Cloud_64.svg",
    "AWS-Route-53": "Arch_Amazon-Route-53_64.svg",
    "AWS-Client-VPN": "Arch_AWS-Client-VPN_64.svg",
    "AWS-App-Mesh": "Arch_AWS-App-Mesh_64.svg",
    "AWS-Direct-Connect": "Arch_AWS-Direct-Connect_64.svg",
    "AWS-Global-Accelerator": "Arch_AWS-Global-Accelerator_64.svg",
    "AWS-Verified-Access": "Arch_AWS-Verified-Access_64.svg",
    "AWS-Transit-Gateway": "Arch_AWS-Transit-Gateway_64.svg",
    "AWS-CloudFront": "Arch_Amazon-CloudFront_64.svg",
    "AWS-Cloud-Map": "Arch_AWS-Cloud-Map_64.svg",
}
